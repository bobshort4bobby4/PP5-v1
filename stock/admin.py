"""
Admin configuration for Stock app
"""


from django.contrib import admin
from .models import Maker, FuelType, Vehicle, Tradein


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    """
    config for Maker admin panel
    """
    list_display = ('maker', 'base_price', 'pk',)


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
    list_display = ('pk',
                    'stock_num',
                    'maker',
                    'model',
                    'year',
                    'fuel',
                    'featured',
                    'available_sale',)

    actions = [
               'set_available_sale_to_true'
               ]

    def set_available_sale_to_true(self, request, queryset):
        queryset.update(available_sale=True)


@admin.register(Tradein)
class TradeinAdmin(admin.ModelAdmin):
    """
    config for Tradein admin panel
    """
    list_display = ('pk', 'user', 'trade_value', 'manufacturer', 'mod',)
