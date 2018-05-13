from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import Parcel
from .views import UntrimmedTiledGeoJSONLayerView, CanvasListView, \
    CanvasserListView, index, canvas_area_define, canvas_sector_define, \
    canvas_details, canvasser_details

urlpatterns = [
    path('', index, name='index'),
    path('canvas-details/<int:canvas_id>/', canvas_details, name='canvas-details'),
    path('canvasser-details/<int:canvasser_id>/', canvasser_details, name='canvasser-details'),
    path('canvas-area/<int:canvas_id>/', canvas_area_define, name='canvas-area'),
    path('canvas-sectors/<int:canvas_id>/', canvas_sector_define, name='canvas-sector'),
    path('canvases/', CanvasListView.as_view(), name='canvases'),
    path('canvassers/', CanvasserListView.as_view(), name='canvassers'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
        UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel),
        name='data_tiled'),
]
