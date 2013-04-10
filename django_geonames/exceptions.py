class InvalidItems(Exception):
    """
    The geonames command will skip item if a city_items_pre_import signal
    receiver raises this exception.
    """
    pass
