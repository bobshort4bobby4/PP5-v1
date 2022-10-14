"""
    Handle context variables
"""
from django.shortcuts import get_object_or_404
from stock.models import Vehicle


def bag_contents(request):
    """
    Handle context variables
    """
    bag_pks = []
    grand_total = 0
    bag = request.session.get('bag', {})
    bag_pks = bag
    bag_items = []

    for item in bag_pks:
        car = get_object_or_404(Vehicle, pk=item)
        grand_total += car.price
        bag_items.append(car)

    flag = request.session['trade_flag']
    if flag:
        trade_value = request.session['trade_details']['trade_value'] 
        grand_total -= trade_value
    minus_grand_total = grand_total * -1
    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'minus_grand_total': minus_grand_total,

    }

    return context
