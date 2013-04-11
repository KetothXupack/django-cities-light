from ..models import Country, Region, City

import autocomplete_light


class CityAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'preferred_name')


class RegionAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'name_ascii')


class CountryAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('name', 'name_ascii')


class RestAutocompleteBase(autocomplete_light. AutocompleteRestModel):
    def model_for_source_url(self, url):
        """
        Return the appropriate model for the urls defined by
        django_geonames.contrib.restframework.urlpatterns.

        Used by RestChannel.
        """
        if 'city/' in url:
            return City
        elif 'region/' in url:
            return Region
        elif 'country/' in url:
            return Country


class CityRestAutocomplete(RestAutocompleteBase, CityAutocomplete):
    pass


class RegionRestAutocomplete(RestAutocompleteBase, RegionAutocomplete):
    pass


class CountryRestAutocomplete(RestAutocompleteBase, RegionAutocomplete):
    pass
