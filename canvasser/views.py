from django.shortcuts import render

from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView

def index(request):
    return render(request, 'canvasser/mainmap.html', {})

class UntrimmedTiledGeoJSONLayerView(TiledGeoJSONLayerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trim_to_boundary = False
