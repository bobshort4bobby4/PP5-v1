from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                    "There's nothing in your bag at the moment")
        return redirect(reverse('stock:stock'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LXn2ACzyNbeBsFOGeW6kpSg258PGQ6Kis0bc4i7yn3Y0f6bSJlA0Ekoepmezx9Bpdyz7CcoubITRkJ726a7HOi9006jVq1ELp',
        'client_secret': "test_secret"

    }

    return render(request, template, context)
