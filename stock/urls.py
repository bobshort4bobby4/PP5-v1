"""
routing paths for stock app
"""
from django.urls import path
from .views import StockView, StockDetailView, EditDeleteView, add_stock, delete_vehicle, edit_vehicle


app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name="stock"),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('add_stock/', add_stock, name='add_stock'),
    path('edit_delete/<int:stock_num>', EditDeleteView.as_view(), name='edit_delete'),
    path('edit/<int:vehicle_id>/', edit_vehicle, name='editvehicle'),
    path('delete/<int:vehicle_id>/',
         delete_vehicle,
         name='delete_vehicle'),

]
