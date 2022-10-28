"""
routing paths for home app
"""
from django.urls import path
from .views import HomeView, LocationView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('location/', LocationView.as_view(), name='location'),
]
