from stock.models import Vehicle
from django.shortcuts import get_object_or_404


def bag_contents(request):
    bag_pks = []
    grand_total = 0
    bag = request.session.get('bag', {})
    bag_pks = bag
    bag_items = []

    for item in bag_pks:
        car = get_object_or_404(Vehicle, pk=item)
        grand_total += car.price
        bag_items.append(car)

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total
    }

    return context
