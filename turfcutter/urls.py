from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import Parcel
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('canvas-pdf/<int:canvas_id>/', canvas_pdf, name='canvas-pdf'),
    path('new-canvas/<int:campaign_id>/', new_canvas, name='new-canvas'),
    path('new-campaign', new_campaign, name='new-campaign'),
    path('new-canvasser', new_canvasser, name='new-canvasser'),
    path('campaign-details/<int:campaign_id>/', campaign_details, name='campaign-details'),
    path('canvas-details/<int:canvas_id>/', canvas_details, name='canvas-details'),
    path('canvasser-details/<int:canvasser_id>/', canvasser_details, name='canvasser-details'),
    path('canvas-area/<int:canvas_id>/', canvas_area_define, name='canvas-area'),
    path('turf/<int:canvas_id>/', turf_define, name='turf'),
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
    path('canvases/', CanvasListView.as_view(), name='canvases'),
    path('canvassers/', CanvasserListView.as_view(), name='canvassers'),
    path('turf-selection/<int:canvas_id>/', turf_select, name='turf-selection'),
    path('turf-canvas/<int:turf_id>/', turf_canvas, name='turf-canvas'),
    path('interaction/<int:turf_id>/<int:parcel_id>/', new_interaction, name='interaction'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
        UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel),
        name='data_tiled'),
]
