"""
    settings for app configuration for stock app
"""

from django.apps import AppConfig


class StockConfig(AppConfig):
    """
    app configuration for stock app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock'
