"""
Settings for this application. The most important is TRANSLATION_LANGUAGES
because it's probably project specific.

TRANSLATION_LANGUAGES
    List of language codes. It is used to generate the alternate_names property
    of django_geonames models. You want to keep it as small as possible.
    By default, it includes the most popular languages according to wikipedia,
    which use a rather ascii-compatible alphabet. It also contains 'abbr' which
    stands for 'abbreviation', you might want to include this one as well.

See:

 - http://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers
 - http://download.geonames.org/export/dump/iso-languagecodes.txt

COUNTRY_SOURCES
    A list of urls to download country info from. Default is countryInfo.txt
    from geonames download server. Overridable in
    settings.GEONAMES_COUNTRY_SOURCES.

REGION_SOURCES
    A list of urls to download region info from. Default is
    admin1CodesASCII.txt from geonames download server. Overridable in
    settings.GEONAMES_REGION_SOURCES

CITY_SOURCES
    A list of urls to download city info from. Default is cities15000.zip from
    geonames download server. Overridable in settings.GEONAMES_CITY_SOURCES

TRANSLATION_SOURCES
    A list of urls to download alternate names info from. Default is
    alternateNames.zip from geonames download server. Overridable in
    settings.GEONAMES_TRANSLATION_SOURCES

SOURCES
    A list with all sources.

DATA_DIR
    Absolute path to download and extract data into. Default is
    django_geonames/data. Overridable in settings.GEONAMES_DATA_DIR

INDEX_SEARCH_NAMES
    If your database engine for django_geonames supports indexing TextFields
    (ie. it is **not** MySQL), then this should be set to True. You might
    have to override this setting if using several databases for your project.
"""

import os.path

from django.conf import settings


def default(key, val):
    return getattr(settings, key, val)

__all__ = ['COUNTRY_SOURCES', 'REGION_SOURCES', 'CITY_SOURCES',
           'TRANSLATION_LANGUAGES', 'TRANSLATION_SOURCES', 'SOURCES', 'DATA_DIR',
           'INDEX_SEARCH_NAMES', 'ISO3166_TO_ISO639', 'CITY_TYPES',
           'NON_ASCII_LANGUAGES', 'ROMANIZED_TO_NATIVE']

COUNTRY_SOURCES = \
    default('CGEONAMES_COUNTRY_SOURCES', ['http://download.geonames.org/export/dump/countryInfo.txt'])
REGION_SOURCES = \
    default('GEONAMES_REGION_SOURCES', ['http://download.geonames.org/export/dump/admin1CodesASCII.txt'])
CITY_SOURCES = \
    default('GEONAMES_CITY_SOURCES', ['http://download.geonames.org/export/dump/cities15000.zip'])
TRANSLATION_SOURCES = \
    default('GEONAMES_TRANSLATION_SOURCES', ['http://download.geonames.org/export/dump/alternateNames.zip'])
TRANSLATION_LANGUAGES = \
    default('GEONAMES_TRANSLATION_LANGUAGES', ['es', 'en', 'pt', 'de', 'pl', 'abbr'])
CITY_TYPES = \
    default('GEONAMES_CITY_TYPES', ['PPL', 'PPLA', 'PPLC', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLG'])


SOURCES = list(COUNTRY_SOURCES) + list(REGION_SOURCES) + list(CITY_SOURCES)
SOURCES += TRANSLATION_SOURCES

# list of ISO3166 country codes. obtained using
#   [c.code2.lower() for c in Country.objects.all()]
DEFAULT_ISO3166 = \
    [u'as', u'aw', u'bb', u'bm', u'bv', u'bz', u'cc', u'ck', u'cx', u'gf', u'gg', u'gi', u'gp', u'gu', u'hm', u'io',
     u'je', u'ky', u'ml', u'mq', u'ms', u'mw', u'nc', u'nf', u'nu', u'pm', u'pn', u'pw', u're', u'ss', u'sj', u'sm',
     u'tc', u'tk', u'to', u'tv', u'ug', u'um', u'yt', u'cs', u'an', u'sy', u'me', u'sl', u'cg', u'lv', u'th', u'dm',
     u'ru', u'im', u'la', u'mg', u'kn', u'es', u'cm', u'fi', u'cd', u'gt', u'mf', u'sb', u'lr', u'is', u'do', u'si',
     u'by', u'pr', u'dj', u'hn', u'id', u'xk', u'hk', u'zw', u'de', u'tz', u'mh', u'uy', u'er', u'mo', u'bq', u'bj',
     u'ee', u'ua', u'eg', u'vi', u'bl', u'sc', u'bo', u'mx', u'bd', u'cr', u'fm', u'bg', u'ch', u'za', u'pa', u'ge',
     u'ie', u'bn', u'jm', u'tm', u'bs', u'ec', u'bt', u'sd', u'ir', u'fr', u'mz', u'cv', u'kz', u'pg', u'sn', u'be',
     u'sg', u'tw', u'wf', u'cz', u'pf', u'pk', u'ni', u'vn', u'dk', u'na', u'fj', u'tn', u'mt', u'kp', u'ly', u'aq',
     u'sr', u'co', u'gl', u'lb', u'br', u'cy', u'il', u'om', u'gh', u'gr', u'mm', u'mk', u'mp', u'ae', u'sh', u'eh',
     u'st', u'ai', u'cf', u'li', u'au', u'lu', u'hr', u'py', u'ne', u'ad', u'ba', u'tg', u'ga', u'kh', u'tr', u'mc',
     u'ph', u'tj', u'ca', u'md', u'kr', u'ar', u'ao', u'pe', u'km', u'cl', u'rs', u'pt', u'ws', u'gd', u'pl', u'so',
     u'ps', u'lk', u'ls', u'ro', u'tt', u'ng', u'sx', u'mr', u'tl', u'gy', u'gw', u'az', u'rw', u'fo', u'ht', u'vg',
     u'lc', u'ax', u'ag', u'kw', u'am', u'al', u'gm', u'dz', u'mn', u'us', u'mu', u'qa', u'bi', u'gs', u'vu', u'sk',
     u'nz', u'iq', u'ye', u'np', u'sv', u'af', u'lt', u'my', u'ke', u'ma', u'sz', u'gb', u'no', u'kg', u'jp', u'nl',
     u'at', u'et', u'hu', u'td', u'zm', u'cn', u'bf', u've', u'sa', u'vc', u'nr', u'ci', u'ki', u'it', u'bw', u'cu',
     u'gq', u'mv', u'fk', u'gn', u'jo', u'bh', u'va', u'in', u'uz', u'cw', u'tf', u'se']

# Fuzzy country code -> language mapping, obtained using
#   {c.code2.lower() : c.languages.split(',')[0].split('-')[0] for c in Country.objects.all() if c.languages}
DEFAULT_ISO3166_TO_ISO639 = \
    {u'gw': u'pt', u'gu': u'en', u'gt': u'es', u'gs': u'en', u'gr': u'el', u'gq': u'es', u'gp': u'fr', u'gy': u'en',
     u'gg': u'en', u'gf': u'fr', u'ge': u'ka', u'gd': u'en', u'gb': u'en', u'ga': u'fr', u'gn': u'fr', u'gm': u'en',
     u'gl': u'kl', u'gi': u'en', u'gh': u'en', u'at': u'de', u'tz': u'sw', u'lc': u'en', u'ma': u'ar', u'la': u'lo',
     u'tv': u'tvl',u'tw': u'zh', u'tt': u'en', u'tr': u'tr', u'lk': u'si', u'li': u'de', u'lv': u'lv', u'to': u'to',
     u'tl': u'tet',u'tm': u'tk', u'lr': u'en', u'tk': u'tkl',u'th': u'th', u'tf': u'fr', u'tg': u'fr', u'td': u'fr',
     u'tc': u'en', u'ly': u'ar', u'do': u'es', u'dm': u'en', u'dj': u'fr', u'dk': u'da', u'de': u'de', u'ye': u'ar',
     u'dz': u'ar', u'mu': u'en', u'yt': u'fr', u'no': u'no', u'vu': u'bi', u'qa': u'ar', u'zm': u'en', u'eh': u'ar',
     u'wf': u'wls',u'ee': u'et', u'eg': u'ar', u'za': u'zu', u'ec': u'es', u'us': u'en', u'et': u'am', u'zw': u'en',
     u'es': u'es', u'er': u'aa', u'ru': u'ru', u'rw': u'rw', u'bh': u'ar', u'rs': u'sr', u're': u'fr', u'it': u'it',
     u'ro': u'ro', u'bd': u'bn', u'be': u'nl', u'bf': u'fr', u'bg': u'bg', u'ba': u'bs', u'bb': u'en', u'ps': u'ar',
     u'bl': u'fr', u'bm': u'en', u'bn': u'ms', u'bo': u'es', u'lu': u'lb', u'bi': u'fr', u'bj': u'fr', u'bt': u'dz',
     u'jm': u'en', u'bw': u'en', u'ws': u'sm', u'bq': u'nl', u'br': u'pt', u'bs': u'en', u'je': u'en', u'by': u'be',
     u'bz': u'en', u've': u'es', u'om': u'ar', u'my': u'ms', u'jo': u'ar', u'ck': u'en', u'xk': u'sq', u'ci': u'fr',
     u'ch': u'de', u'co': u'es', u'cn': u'zh', u'cm': u'en', u'cl': u'es', u'cc': u'ms', u'ca': u'en', u'cg': u'fr',
     u'cf': u'fr', u'cd': u'fr', u'cz': u'cs', u'cy': u'el', u'cx': u'en', u'cs': u'cu', u'cr': u'es', u'cw': u'nl',
     u'cv': u'pt', u'cu': u'es', u'ad': u'ca', u'pr': u'en', u'tn': u'ar', u'pw': u'pau',u'pt': u'pt', u'py': u'es',
     u'lt': u'lt', u'ls': u'en', u'iq': u'ar', u'pa': u'es', u'pf': u'fr', u'pg': u'en', u'pe': u'es', u'pk': u'ur',
     u'ph': u'tl', u'pn': u'en', u'pl': u'pl', u'pm': u'fr', u'vc': u'en', u'hr': u'hr', u'ht': u'ht', u'hu': u'hu',
     u'hk': u'zh', u'hn': u'es', u'ao': u'pt', u'jp': u'ja', u'lb': u'ar', u'me': u'sr', u'md': u'ro', u'mg': u'fr',
     u'mf': u'fr', u'uy': u'es', u'mc': u'fr', u'uz': u'uz', u'mm': u'my', u'ml': u'fr', u'mo': u'zh', u'mn': u'mn',
     u'mh': u'mh', u'mk': u'mk', u'um': u'en', u'mt': u'mt', u'mw': u'ny', u'mv': u'dv', u'mq': u'fr', u'mp': u'fil',
     u'ms': u'en', u'mr': u'ar', u'au': u'en', u'ug': u'en', u'ua': u'uk', u'mx': u'es', u'mz': u'pt', u'va': u'la',
     u'sa': u'ar', u'ae': u'ar', u'io': u'en', u'ag': u'en', u'vg': u'en', u'ai': u'en', u'vi': u'en', u'is': u'is',
     u'ir': u'fa', u'am': u'hy', u'al': u'sq', u'vn': u'vi', u'an': u'nl', u'as': u'en', u'ar': u'es', u'im': u'en',
     u'il': u'he', u'aw': u'nl', u'in': u'en', u'ax': u'sv', u'az': u'az', u'ie': u'en', u'id': u'id', u'ni': u'es',
     u'nl': u'nl', u'kr': u'ko', u'na': u'en', u'nc': u'fr', u'ne': u'fr', u'nf': u'en', u'ng': u'en', u'nz': u'en',
     u'sh': u'en', u'np': u'ne', u'kw': u'ar', u'nr': u'na', u'nu': u'niu',u'fr': u'fr', u'af': u'fa', u'sv': u'es',
     u'kz': u'kk', u'fi': u'fi', u'fj': u'en', u'fk': u'en', u'fm': u'en', u'fo': u'fo', u'tj': u'tg', u'sz': u'en',
     u'sy': u'ar', u'sx': u'nl', u'kg': u'ky', u'ke': u'en', u'ss': u'en', u'sr': u'nl', u'ki': u'en', u'kh': u'km',
     u'kn': u'en', u'km': u'ar', u'st': u'pt', u'sk': u'sk', u'sj': u'no', u'si': u'sl', u'kp': u'ko', u'so': u'so',
     u'sn': u'fr', u'sm': u'it', u'sl': u'en', u'sc': u'en', u'sb': u'en', u'ky': u'en', u'sg': u'cmn',u'se': u'sv',
     u'sd': u'ar'}

ISO3166_TO_ISO639 = default('GEONAMES_ISO3166_TO_ISO639', DEFAULT_ISO3166_TO_ISO639)

DATA_DIR = getattr(settings, 'GEONAMES_DATA_DIR',
                   os.path.normpath(os.path.join(
                       os.path.dirname(os.path.realpath(__file__)), 'data')))

NON_ASCII_LANGUAGES = default('GEONAMES_NON_ASCII_LANGUAGES',
                              [k for (k, v) in DEFAULT_ISO3166_TO_ISO639.items() if v != 'en'])
ROMANIZED_TO_NATIVE = default('GEONAMES_ROMANIZED_TO_NATIVE',
                              [k for (k, v) in DEFAULT_ISO3166_TO_ISO639.items() if v == 'en'])

# FIXME: to be removed after migrations join
INDEX_SEARCH_NAMES = False
