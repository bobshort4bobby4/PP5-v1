"""
Admin configuration for Stock app
"""


from django.contrib import admin
from .models import Maker, FuelType, Vehicle


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    """
    config for Maker admin panel
    """
    list_display = ('maker', 'pk',)


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    """
    config for FuelType admin panel
    """
    list_display = ('fuel', 'pk',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """
    config for Vehicle admin panel
    """
    list_display = ('stock_num', 'maker', 'model', 'year', 'fuel','featured',)
