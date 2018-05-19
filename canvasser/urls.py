from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import Parcel
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('new-campaign', new_campaign, name='new-campaign'),
    path('campaign-details/<int:campaign_id>/', campaign_details, name='campaign-details'),
    path('canvas-details/<int:canvas_id>/', canvas_details, name='canvas-details'),
    path('canvasser-details/<int:canvasser_id>/', canvasser_details, name='canvasser-details'),
    path('canvas-area/<int:canvas_id>/', canvas_area_define, name='canvas-area'),
    path('turf/<int:canvas_id>/', turf_define, name='turf'),
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
    path('canvases/', CanvasListView.as_view(), name='canvases'),
    path('canvassers/', CanvasserListView.as_view(), name='canvassers'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
        UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel),
        name='data_tiled'),
]
