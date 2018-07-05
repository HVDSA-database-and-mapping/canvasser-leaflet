from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import Parcel
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('canvass-pdf/<int:canvass_id>/', canvass_pdf, name='canvass-pdf'),
    path('new-canvass/<int:campaign_id>/', new_canvass, name='new-canvass'),
    path('new-campaign', new_campaign, name='new-campaign'),
    path('new-canvasser', new_canvasser, name='new-canvasser'),
    path('campaign-details/<int:campaign_id>/', campaign_details, name='campaign-details'),
    path('canvass-details/<int:canvass_id>/', canvass_details, name='canvass-details'),
    path('canvasser-details/<int:canvasser_id>/', canvasser_details, name='canvasser-details'),
    path('canvass-area/<int:canvass_id>/', canvass_area_define, name='canvass-area'),
    path('turf/<int:canvass_id>/', turf_define, name='turf'),
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
    path('canvasses/', CanvassListView.as_view(), name='canvasses'),
    path('canvassers/', CanvasserListView.as_view(), name='canvassers'),
    path('turf-selection/<int:canvass_id>/', turf_select, name='turf-selection'),
    path('turf-canvass/<int:turf_id>/', turf_canvass, name='turf-canvass'),
    path('interaction/<int:turf_id>/<int:parcel_id>/', new_interaction, name='interaction'),
    path('turf-interactions/<int:turf_id>/', turf_interactions, name='turf-interactions'),
    re_path(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
        UntrimmedTiledGeoJSONLayerView.as_view(model=Parcel),
        name='data_tiled'),
]
