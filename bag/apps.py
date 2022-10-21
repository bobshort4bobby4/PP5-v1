
"""Configures the app"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """Initialise app settings"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
