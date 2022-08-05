from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    config for Maker admin panel
    """
    list_display = ('pk', 'default_phone_number',)
