"""
routing paths for stock app
"""
from django.urls import path
from .views import StockView, StockDetailView


app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name="stock"),
    path('<pk>/', StockDetailView.as_view(), name='stock_detail'),

]
