from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Canvas, Canvasser, CanvasArea, Parcel, CanvasSector
from djgeojson.views import TiledGeoJSONLayerView
from django.contrib.gis.db.models.functions import AsGeoJSON, Transform 

import datetime

from .forms import NewCanvasForm, CanvasAreaForm, CanvasSectorForm


class UntrimmedTiledGeoJSONLayerView(TiledGeoJSONLayerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trim_to_boundary = False


class CanvasListView(generic.ListView):
    model = Canvas


class CanvasserListView(generic.ListView):
    model = Canvasser


def index(request):

    if request.method == 'POST':
        form = NewCanvasForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # (here we just write it to the model due_back field)
            canvas_inst = form.save(commit=False)
            canvas_inst.owner = request.user
            canvas_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/canvasser/canvas-area/%d/' % canvas_inst.id)

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCanvasForm()

    return render(request, 'canvasser/index.html',
        {'form': form})

def canvas_details(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_parcels = Parcel.objects.filter(geom__intersects=this_canvas_area.geom).order_by('prop_street', 'prop_street_num')
    return render(request, 'canvasser/canvas_details.html', {'canvas': this_canvas, 'parcels': these_parcels})

def canvas_area_define(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    if request.method == 'POST':
        form = CanvasAreaForm(request.POST)
        if form.is_valid():
            canvas_area = form.save(commit=False)
            canvas_area.canvas_id = canvas_id
            canvas_area.save()
            return HttpResponseRedirect('/canvasser/canvas-sectors/%d/' % canvas_id)
    else:
        form = CanvasAreaForm()
    return render(request, 'canvasser/canvas_area.html', {'form': form})

def canvas_sector_define(request, canvas_id):
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_parcels = Parcel.objects.filter(geom__intersects=this_canvas_area.geom)
    these_sectors = CanvasSector.objects.filter(canvas_id=canvas_id)
    if request.method == 'POST':
        form = CanvasSectorForm(request.POST)
        if form.is_valid():
            canvas_sector = form.save(commit=False)
            canvas_sector.canvas_id = canvas_id
            canvas_sector.order = 0
            canvas_sector.save()
            form.save_m2m()
            return HttpResponseRedirect('/canvasser/canvas-sectors/%d/' % canvas_id)
    else:
        form = CanvasSectorForm()
    return render(request, 'canvasser/canvas_sector.html', 
            {'form': form, 
            'canvas_area': this_canvas_area, 
            'canvas_id': canvas_id,
            'parcels': these_parcels,
            'sectors': these_sectors})
