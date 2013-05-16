import unicodedata
import re

from django.utils.encoding import force_unicode
from django.db.models import signals
from django.db import models
from django.utils.translation import ugettext as _

from south.modelsinspector import introspector

import autoslug

__all__ = ['Country', 'Region', 'City', 'CONTINENT_CHOICES',
           'to_ascii']

ALPHA_REGEXP = re.compile('[\W_]+', re.UNICODE)

CONTINENT_CHOICES = (
    ('OC', _(u'Oceania')),
    ('EU', _(u'Europe')),
    ('AF', _(u'Africa')),
    ('NA', _(u'North America')),
    ('AN', _(u'Antarctica')),
    ('SA', _(u'South America')),
    ('AS', _(u'Asia')),
)


def to_ascii(value):
    if isinstance(value, str):
        value = force_unicode(value)

    return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')


def set_name_ascii(sender, instance=None, **kwargs):
    """
    Signal receiver that sets instance.name_ascii from instance.name.

    Ascii versions of names are often useful for autocompletes and search.
    """

    name_ascii = to_ascii(instance.name)
    if name_ascii and not instance.name_ascii:
        instance.name_ascii = to_ascii(instance.name)


def set_display_name(sender, instance=None, **kwargs):
    """
    Set instance.display_name to instance.get_display_name(), avoid spawning
    queries during __unicode__().
    """
    instance.display_name = instance.get_display_name()


class Base(models.Model):
    """
    Base model with boilerplate for all models.
    """

    name_ascii = models.CharField(max_length=200, blank=True, db_index=True)

    slug = autoslug.AutoSlugField(populate_from='name_ascii')
    geoname_id = models.IntegerField(null=True, blank=True, unique=True)

    preferred_name = models.CharField(_('Native name'), max_length=200, blank=True, db_index=True)
    update_preferred_name = models.BooleanField(_('Allow native name to be automatically updated'),
                                                null=False, blank=False, default=True)

    reg_enabled = models.BooleanField(_('Registration is enabled for this entity'),
                                      null=False, blank=False, default=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        display_name = getattr(self, 'display_name', None)
        if display_name:
            return display_name
        # noinspection PyUnresolvedReferences
        return self.name


class Country(Base):
    """
    Country model.
    """

    name = models.CharField(max_length=200, unique=True)

    code2 = models.CharField(_('ISO 3166-1 alpha-2'), max_length=2, null=True, blank=True, unique=True)
    code3 = models.CharField(_('ISO 3166-1 alpha-3'), max_length=3, null=True, blank=True, unique=True)
    continent = models.CharField(max_length=2, db_index=True, choices=CONTINENT_CHOICES)
    tld = models.CharField(max_length=5, blank=True, db_index=True)

    currency_code = models.CharField(max_length=5, blank=True, db_index=True)
    currency_name = models.CharField(max_length=15, blank=True)

    population = models.IntegerField(null=False, blank=False, default=0)
    languages = models.CharField(_('Comma-separated list of languages'), max_length=150, blank=True)

    phone_code = models.IntegerField(_('Calling code'), null=True, blank=True, default=0)
    phone_enabled = models.BooleanField(_('Registration using phone is enabled for this entity'),
                                        null=False, blank=False, default=True)

    class Meta:
        verbose_name_plural = _(u'countries')
        #db_table = 'dm_country'


signals.pre_save.connect(set_name_ascii, sender=Country)


class Region(Base):
    """
    Region/State model.
    """

    name = models.CharField(max_length=200, db_index=True)
    display_name = models.CharField(max_length=200)
    geoname_code = models.CharField(max_length=50, null=True, blank=True, db_index=True)

    country = models.ForeignKey(Country)

    class Meta:
        unique_together = (('country', 'name'), )
        verbose_name = _('region/state')
        verbose_name_plural = _('regions/states')
        #db_table = 'dm_region'

    def get_display_name(self):
        return u'%s, %s' % (self.name, self.country.name)


signals.pre_save.connect(set_name_ascii, sender=Region)
signals.pre_save.connect(set_display_name, sender=Region)


# FIXME: to be removed after migrations join
class ToSearchTextField(models.TextField):
    """
    Trivial TextField subclass that passes values through to_search
    automatically.
    """

    def south_field_triple(self):
        """Returns a suitable description of this field for South."""

        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        args, kwargs = introspector(self)
        # That's our definition!
        return field_class, args, kwargs


class City(Base):
    """
    City model.
    """

    name = models.CharField(max_length=200, db_index=True)
    display_name = models.CharField(max_length=200)

    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)

    timezone = models.CharField(max_length=40, blank=True)

    region = models.ForeignKey(Region, blank=True, null=True)
    country = models.ForeignKey(Country)

    population = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        unique_together = (('region', 'name'),)
        verbose_name_plural = _(u'cities')
        #db_table = 'dm_city'

    def get_display_name(self):
        if self.region_id:
            return u'%s, %s, %s' % (self.name, self.region.name,
                                    self.country.name)
        else:
            return u'%s, %s' % (self.name, self.country.name)


signals.pre_save.connect(set_name_ascii, sender=City)
signals.pre_save.connect(set_display_name, sender=City)


def city_country(sender, instance, **kwargs):
    if instance.region_id and not instance.country_id:
        instance.country = instance.region.country


signals.pre_save.connect(city_country, sender=City)
