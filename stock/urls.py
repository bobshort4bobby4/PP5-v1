"""
routing paths for stock app
"""
from django.urls import path
from .views import StockView


app_name = 'stock'

urlpatterns = [
    path('', StockView.as_view(), name="stock"),

]
