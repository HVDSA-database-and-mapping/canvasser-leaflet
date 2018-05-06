from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import CensusTract, Parcel
from .views import UntrimmedTiledGeoJSONLayerView
from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView

urlpatterns = [
    path('', TemplateView.as_view(template_name='canvasser/mainmap.html'), name='mainmap'),
    path('data.geojson', GeoJSONLayerView.as_view(model=CensusTract), name='data'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$', UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel), name='data_tiled'),
]
