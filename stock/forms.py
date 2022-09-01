from django import forms
from .models import Vehicle, Maker, FuelType


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'