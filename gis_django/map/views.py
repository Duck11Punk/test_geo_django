from django.shortcuts import render
from django.contrib.gis.utils import LayerMapping
from .models import Map
import os


def load():
    """ Creates a database representation of shapefile """

    # To run this command type: 'python manage.py shell'
    # 'from map.views import load; load()'

    mapping = {"productivi": "productivi", "mpoly": "MULTIPOLYGON"}
    map_path = os.path.abspath('gis_django/fields_test/test_fields.shp')
    lm = LayerMapping(Map, map_path, mapping, transform=False, encoding="iso-8859-1")
    lm.save(verbose=True)
