from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import CensusTract, Parcel
from .views import UntrimmedTiledGeoJSONLayerView
from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='canvasser/index.html'), name='index'),
    path('canvases/', views.CanvasListView.as_view(), name='canvases'),
    path('canvassers/', views.CanvasserListView.as_view(), name='canvassers'),
    path('data.geojson', GeoJSONLayerView.as_view(model=CensusTract), name='data'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$', UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel), name='data_tiled'),
]
