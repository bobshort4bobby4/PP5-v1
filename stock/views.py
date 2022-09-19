
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.http import HttpResponse
from django.conf import settings

from django.db.models import Q
from stock.models import Vehicle, Maker
from .forms import VehicleForm
from .trade_calc import calc_tradein

# from stock.models import Vehicle


class StockView(ListView):
    """
    Generic class used to display vehicle display page

    """

    def get_queryset(self):
        queryset = Vehicle.objects.filter(available_sale=True)
        super().get_queryset()

        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                               ("You didn't enter any search criteria!"))
                return queryset

            vector = SearchVector("maker__maker", "model", "fuel__fuel", "year")
            query = SearchQuery(query)
            queryset = Vehicle.objects.filter(available_sale=True).annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')
        

        return queryset

    model = Vehicle
    template_name = "stock/stock.html"


class StockDetailView(DetailView):
    """
    Generic class used to display vehicle detail page

    """
    model = Vehicle
    template_name = "stock/stock_detail.html"


def add_stock(request):

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            veh = form.save()
            messages.success(request, 'Successfully added Vehicle!')
            return redirect(reverse('stock:stock_detail', args=[veh.stock_num]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = VehicleForm()

    template = 'stock/add_stock.html'
    context = {
        'form': form
    }

    return render(request, template, context)


class EditDeleteView(View):

    def get(self, request, stock_num):
        veh = get_object_or_404(Vehicle, pk=stock_num)
        template = 'stock/edit_delete.html'
        form = VehicleForm(instance=veh)
        context = {
            'form': form,
        }
        return render(request, template, context)


def delete_vehicle(request, vehicle_id):
    """ Delete a vehicle from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store staff can do that.')
        return redirect(reverse('home:home'))

    veh = get_object_or_404(Vehicle, pk=vehicle_id)
    veh.available_sale = False
    veh.save()
    messages.success(request, 'Vehicle Deleted!')
    return redirect(reverse('stock:stock'))



def edit_vehicle(request, vehicle_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store staff can do that.')
        return redirect(reverse('home:home'))

    veh = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        veh = get_object_or_404(Vehicle, pk=vehicle_id)
        form = VehicleForm(request.POST, request.FILES, instance=veh)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Vehicle!')
            return redirect(reverse('stock:stock_detail', args=[veh.pk]))
        else:
            messages.error(request,
                        ('Failed to update Vehicle. '
                            'Please ensure the form is valid.'))
    else:
        form = VehicleForm(instance=veh)
        # messages.info(request, f'You are editing {productvehicle.name}')

    template = 'stock/edit_vehicle.html'
    context = {
        'form': form,
        'vehicle': veh,
        'vehicle_id': veh.pk,
    }

    return render(request, template, context)


def trade_in(request):
    template = 'stock/trade_in.html'
    makes = Maker.objects.all()

    context = {
        'makes': makes,
    }

    return render(request, template, context)


def trade_value(request):

    manu = request.POST.get('inputmanu')
    model = request.POST.get('inputmodel')
    year = request.POST.get('inputyear')
    odo = request.POST.get('inputodo')
    condition = request.POST.get('inlineRadioOptions')
    trade_val, full_price = calc_tradein(manu, year, odo, condition)
    flag = settings.TRADE_FLAG
    if flag is True:
        return HttpResponse("Sorry one trade-in per order.")

    else:
        trade_details = {
        'manufacturer': manu,
        'model': model,
        'year': year,
        'odo': odo,
        'condition': condition,
        'trade_value': trade_val,
        'full_price': full_price,
        }
        if trade_val == 0:
            head = "Sorry"
            mess = "Your Vehicle is too old for us to offer any Trade-in"
            lnk = '''<a id="allvehlink" href="/stock/trade_in/" class="btn btn-outline-black rounded-0 mt-2">
                        <span class="icon">
                        <i class="fas fa-chevron-left"></i>
                        </span>
                        <span class="text-uppercase">Value Another Vehicle</span>
                        </a>'''
        else:
            head = "Great News !"
            mess = f"We can offer €{ trade_val } (subject to inspection) for your vehicle as credit on any vahicle valued over €{ full_price }"
            lnk = f'<div class="text-center"><a type="submit" class="btn btn-primary my-2" hx-post="/stock/take_trade/" hx-target="#trade-value">Take The Trade</a></div>'

        request.session['trade_details'] = trade_details
        return HttpResponse(f'<h1 class="text-center text-white">{ head }</h1>'
                            f"<p>{ mess }</p>"
                            f"{ lnk }"
                            )


def take_trade(request):
    messages.success(request, 'Successfully Traded Vehicle!')
    trade_details = request.session['trade_details']
    settings.TRADE_FLAG = True

    return HttpResponse('<div><h1 class="text-center">ThankYou</h1></div>'
                        ''' <div>
                        <a id="allvehlink" href="/stock/trade_in/" class="btn btn-outline-black rounded-0 mt-2">
                        <span class="icon">
                        <i class="fas fa-chevron-left"></i>
                        </span>
                        <span class="text-uppercase">Value Another Vehicle</span>
                        </a>
                        </div>''')

def clear_trade(request):
    settings.TRADE_FLAG = False
    messages.success(request, 'Cleared Trade-ins')
    return redirect(reverse('stock:trade_in'))