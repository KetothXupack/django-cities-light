from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .forms import *
from .models import *


class CountryAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Country.
    """

    list_display = (
        'name',
        'preferred_name',
        'code2',
        'code3',
        'continent',
        'tld',
        'population'
    )
    search_fields = (
        'name',
        'name_ascii',
        'preferred_name',
        'code2',
        'code3',
        'tld'
    )
    list_filter = (
        'continent',
    )
    form = CountryForm
admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    """
    ModelAdmin for Region.
    """
    list_filter = (
        'country__continent',
        'country',
    )
    search_fields = (
        'name',
        'preferred_name',
        'country__preferred_name',
        'country__name',
        'name_ascii',
    )
    list_display = (
        'name',
        'preferred_name',
        'country',
    )
    form = RegionForm
admin.site.register(Region, RegionAdmin)


class CityChangeList(ChangeList):
    pass


class CityAdmin(admin.ModelAdmin):
    """
    ModelAdmin for City.
    """
    list_display = (
        'name',
        'preferred_name',
        'region',
        'country',
        'population'
    )
    search_fields = (
        'name',
        'preferred_name',
        'name_ascii',
        'country__preferred_name',
        'country__name',
        'region__preferred_name',
        'region__name',
    )
    list_filter = (
        'country__continent',
        'country',
    )
    form = CityForm

    def get_changelist(self, request, **kwargs):
        return CityChangeList

admin.site.register(City, CityAdmin)
