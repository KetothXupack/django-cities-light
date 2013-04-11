"""
Couples django_geonames and django-ajax-selects.

Register the lookups in settings.AJAX_LOOKUP_CHANNELS, add::

    'django_geonames_country': ('django_geonames.lookups', 'CountryLookup'),
    'django_geonames_city': ('django_geonames.lookups', 'CityLookup'),
"""

from ajax_select import LookupChannel
from django.db.models import Q

from ..models import *


class StandardLookupChannel(LookupChannel):
    """
    Honnestly I'm not sure why this is here.
    """

    def format_match(self, obj):
        """ (HTML) formatted item for displaying item in the dropdown """
        return self.get_result(obj)

    def format_item_display(self, obj):
        """
        (HTML) formatted item for displaying item in the selected deck area
        """
        return self.get_result(obj)


class CountryLookup(StandardLookupChannel):
    """
    Lookup channel for Country, hits name and name_ascii.
    """

    model = Country

    def get_query(self, q, request):
        return Country.objects.filter(
            Q(name__icontains=q)
            | Q(name_ascii__icontains=q)
            | Q(preferred_name__icontains=q)
            | Q(display_name_ascii__icontains=q)
        ).distinct()


class RegionLookup(StandardLookupChannel):
    """
    Lookup channel for Region, hits name and name_ascii.
    """

    model = Region

    def get_query(self, q, request):
        return Region.objects.filter(
            Q(name__icontains=q)
            | Q(name_ascii__icontains=q)
            | Q(preferred_name__icontains=q)
            | Q(display_name_ascii__icontains=q)
        ).distinct()


class CityLookup(StandardLookupChannel):
    """
    Lookup channel for City, hits name and search_names.
    """
    model = City

    def get_query(self, q, request):
        return City.objects.filter(
            Q(name__icontains=q)
            | Q(name_ascii__icontains=q)
            | Q(preferred_name__icontains=q)
            | Q(display_name_ascii__icontains=q)
        ).select_related('country').distinct()
