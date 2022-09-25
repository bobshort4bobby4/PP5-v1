from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.views.generic import TemplateView
from stock.models import Vehicle


class BagView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # check to see it trade-in has been made
        flag = settings.TRADE_FLAG
        if flag is True:
            context['trade_value'] = self.request.session['trade_details']['trade_value']
            context['minustrade_value'] = context['trade_value'] * -1
            context['sub_tot'] = context['trade_value']
        else:
            context['trade_value'] = {}
            context['minustrade_value'] = 0
            context['sub_tot'] = 0 
        
        return context
    template_name = 'bag/bag.html'


def add_to_bag(request, item_id):
    """ Add selected vehicle to the shopping bag """
    veh = get_object_or_404(Vehicle, pk=item_id)

    bag = request.session.get('bag', [])

    if item_id in bag:
        messages.error(
                    request, f'This Vehicle  {veh.maker} {veh.model} \
                         is already in your bag')
        return redirect(reverse('stock:stock'))
    else:
        bag.append(item_id)

    request.session['bag'] = bag
    listboughtveh = bag
    for item in listboughtveh:
        car = get_object_or_404(Vehicle, pk=item)
        print(f"{car.maker} {car.model}")
    messages.success(
                    request, f'Added {veh.maker} {veh.model} to your bag')
    return redirect(reverse('stock:stock'))


def remove_from_bag(request, item_id):
    """ remove selected vehicle from bag  """
    bag = list(request.session.get('bag', []))
    veh = get_object_or_404(Vehicle, pk=item_id)

    bag.remove(item_id)
    request.session['bag'] = bag

    messages.success(
                    request, f'Removed {veh.maker} {veh.model} from your bag')
    return redirect(reverse('bag:bag'))
