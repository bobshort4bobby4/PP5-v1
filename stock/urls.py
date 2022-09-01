"""
routing paths for stock app
"""
from django.urls import path
from .views import StockView, StockDetailView, add_stock


app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name="stock"),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('add_stock/', add_stock, name='add_stock'),

]
