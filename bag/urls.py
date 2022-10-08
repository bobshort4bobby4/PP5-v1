"""
routing paths for bag app
"""
from django.urls import path
from . views import BagView, add_to_bag, remove_from_bag, clear_trade_bag


app_name = 'bag'

urlpatterns = [
     path('', BagView.as_view(), name='bag'),
     path('add/<item_id>/', add_to_bag, name='add_to_bag'),
     path('remove/<item_id>/', remove_from_bag, name='remove_from_bag'),
     path('clear_trade_bag/', clear_trade_bag, name='clear_trade_bag')

]
