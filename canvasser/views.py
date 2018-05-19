from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from djgeojson.views import TiledGeoJSONLayerView
from django.contrib.gis.db.models.functions import AsGeoJSON, Transform 

import datetime

from .forms import *


class UntrimmedTiledGeoJSONLayerView(TiledGeoJSONLayerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trim_to_boundary = False


class CanvasListView(generic.ListView):
    model = Canvas


class CanvasserListView(generic.ListView):
    model = Canvasser


class CampaignListView(generic.ListView):
    model = Campaign


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

def new_campaign(request):

    if request.method == 'POST':
        form = NewCampaignForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # (here we just write it to the model due_back field)
            campaign_inst = form.save(commit=False)
            campaign_inst.owner = request.user
            campaign_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/canvasser/campaigns/')

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCampaignForm()

    return render(request, 'canvasser/new_campaign.html',
        {'form': form})

def campaign_details(request, campaign_id):
    this_campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'canvasser/campaign_details.html', {'campaign': this_campaign})

def canvas_details(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_parcels = Parcel.objects.filter(geom__intersects=this_canvas_area.geom).order_by('prop_street', 'prop_street_num')
    return render(request, 'canvasser/canvas_details.html', {'canvas': this_canvas, 'parcels': these_parcels})

def canvasser_details(request, canvasser_id):
    this_canvasser = get_object_or_404(Canvasser, id=canvasser_id)
    return render(request, 'canvasser/canvasser_details.html', {'canvasser': this_canvasser})
    

def canvas_area_define(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    if request.method == 'POST':
        form = CanvasAreaForm(request.POST)
        if form.is_valid():
            canvas_area = form.save(commit=False)
            canvas_area.canvas_id = canvas_id
            canvas_area.save()
            return HttpResponseRedirect('/canvasser/turf/%d/' % canvas_id)
    else:
        form = CanvasAreaForm()
    return render(request, 'canvasser/canvas_area.html', {'form': form})

def turf_define(request, canvas_id):
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_parcels = Parcel.objects.filter(geom__intersects=this_canvas_area.geom)
    these_turfs = Turf.objects.filter(canvas_id=canvas_id)
    if request.method == 'POST':
        form = TurfForm(request.POST)
        if form.is_valid():
            turf = form.save(commit=False)
            turf.canvas_id = canvas_id
            turf.save()
            form.save_m2m()
            return HttpResponseRedirect('/canvasser/turf/%d/' % canvas_id)
    else:
        form = TurfForm()
    return render(request, 'canvasser/turf.html', 
            {'form': form, 
            'canvas_area': this_canvas_area, 
            'canvas_id': canvas_id,
            'parcels': these_parcels,
            'turfs': these_turfs})
