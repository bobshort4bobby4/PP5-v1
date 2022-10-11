"""
Forms for stock app
"""

from django import forms
from .models import Vehicle, Maker


class VehicleForm(forms.ModelForm):
    """
    Form for Vehicle model
    """

    class Meta:
        """
        settings for Vehicleform
        """
        model = Vehicle
        fields = '__all__'


class MakerForm(forms.ModelForm):
    """
    Form for maker model
    """

    class Meta:
        """
        settings for MakerForm
        """
        model = Maker
        fields = '__all__'
