from django.urls import path
from django.views.generic import TemplateView
from .models import CensusTract
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    path('', TemplateView.as_view(template_name='canvas_planner/mainmap.html'), name='mainmap'),
    path('data.geojson', GeoJSONLayerView.as_view(model=CensusTract), name='data'),
]
