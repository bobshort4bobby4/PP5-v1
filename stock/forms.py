from django import forms
from .models import Vehicle, Maker, FuelType


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'


class MakerForm(forms.ModelForm):

    class Meta:
        model = Maker
        fields = '__all__'
