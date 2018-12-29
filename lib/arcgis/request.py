import requests
from functools import partial

from .const import ARCGIS_URL_PREF
from .response import ArcGISResponse


def make_fetch_url_scalar(id_obj):
    return '%s&objectids=%d'% (ARCGIS_URL_PREF, id_obj)

def make_fetch_url_range(id_obj_start, id_obj_finish):
    return '%s&where=objectid>%d+and+objectid<=%d' % (
        ARCGIS_URL_PREF, id_obj_start, id_obj_finish
    )

def _fetch(url_maker, *args, **kwargs):
    url = url_maker(*args, **kwargs)
    return ArcGISResponse(requests.get(url).json())
    
fetch_row = partial(_fetch, make_fetch_url_scalar)
fetch_range = partial(_fetch, make_fetch_url_range)

