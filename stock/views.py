
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages

from django.db.models import Q
from stock.models import Vehicle
from .forms import VehicleForm

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
            # attempt to implement muli-term search
            terms = self.request.GET['q'].split(' ')

            field_names = ["maker__maker", "model", "fuel__fuel", "year"]
            or_query = None
            query = None
            for term in terms:
                for field in field_names:
                    q = Q(**({"%s__icontains" % field: term}))
                    if or_query is None:
                        or_query = q
                    else:
                        or_query = or_query | q
                if query is None:
                    query = or_query
                else:
                    query = query and or_query
            queries = query
            vehicles = Vehicle.objects.filter(available_sale=True)
            queryset = vehicles.filter(queries)

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
    """ Delete a product from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store staff can do that.')
        return redirect(reverse('home:home'))

    veh = get_object_or_404(Vehicle, pk=vehicle_id)
    veh.delete()
    messages.success(request, 'Vehicle Deleted!')
    return redirect(reverse('stock:stock'))



def edit_vehicle(request, vehicle_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store staff can do that.')
        return redirect(reverse('home:home'))

    veh = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=veh)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Vehicle!')
            return redirect(reverse('stock:stock_detail', args=[veh.id]))
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
    }

    return render(request, template, context)