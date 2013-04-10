from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()


def get_flag(iso, flag_path=u''):
    """
    Returns a full path to the ISO 3166-1 alpha-2 country code flag image.

    ``flag_path`` is given in the form
    ``'<path relative to media root>/%s.png'``
    and is appended to ``settings.STATIC_URL``

    if a valid flag_path is not given tries to use
    ``settings.COUNTRIES_FLAG_PATH``
    defaults to ``'flags/%s.gif'``
    """

    if not settings.STATIC_URL:
        return u''
    default = u'-'
    if not iso:
        iso = default
    else:
        iso = iso.lower().strip()
    try:
        flag_name = flag_path % iso
    except (ValueError, TypeError):
        flag_path = getattr(settings, 'COUNTRIES_FLAG_PATH', u'flags/%s.png')
        try:
            flag_name = flag_path % iso
        except (ValueError, TypeError):
            return u''
    return u''.join((settings.STATIC_URL, 'flags', flag_name))


@stringfilter
def iso_flag(iso, flag_path=u''):
    """
    Returns a full path to the ISO 3166-1 alpha-2 country code flag image.

    Example usage::

        {{ country.code2|iso_flag }}

        {{ country.code2|iso_flag:"static/flags/%s.png" }}
    """

    return get_flag(iso, flag_path)


register.filter('iso_flag', iso_flag)
