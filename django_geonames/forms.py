from django import forms

from .models import Country, Region, City

__all__ = ['CountryForm', 'RegionForm', 'CityForm']


class CountryForm(forms.ModelForm):
    """
    Country model form.
    """
    class Meta:
        model = Country
        fields = ('name', 'continent', 'preferred_name', 'update_preferred_name')


class RegionForm(forms.ModelForm):
    """
    Region model form.
    """
    class Meta:
        model = Region
        fields = ('name', 'country', 'preferred_name', 'update_preferred_name')


class CityForm(forms.ModelForm):
    """
    City model form.
    """
    class Meta:
        model = City
        fields = ('name', 'region', 'country', 'preferred_name', 'update_preferred_name',
                  'latitude', 'longitude', 'timezone')
