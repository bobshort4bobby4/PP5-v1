"""
routing paths for stock app
"""
from django.urls import path
from .views import (StockView,
                    StockDetailView,
                    # EditDeleteView,
                    add_stock,
                    # delete_vehicle,
                    clear_trade,
                    edit_vehicle,
                    trade_in,
                    trade_value,
                    take_trade,
                    adjust_tradein,
                    DeleteVehicleView)


app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name='stock'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('add_stock/', add_stock, name='add_stock'),
    path('edit/<int:vehicle_id>/', edit_vehicle, name='edit_vehicle'),
    path('delete/<int:vehicle_id>/',
         DeleteVehicleView.as_view(),
         name='delete_vehicle'),
    path('trade_in/', trade_in, name='trade_in'),
    path('trade_value/', trade_value, name='trade_value'),
    path('take_trade/', take_trade, name='take_trade'),
    path('clear_trade/', clear_trade, name='clear_trade'),
    path('adjust_tradein/', adjust_tradein, name='adjust_tradein'),

]
