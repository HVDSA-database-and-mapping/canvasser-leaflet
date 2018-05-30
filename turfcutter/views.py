from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import *
from djgeojson.views import TiledGeoJSONLayerView
from django.contrib.gis.db.models.functions import AsGeoJSON, Transform

import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors

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


def new_canvasser(request):

    if request.method == 'POST':
        form = NewCanvasserForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # (here we just write it to the model due_back field)
            canvasser_inst = form.save(commit=False)
            canvasser_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/turfcutter/canvasser-details/%d/' % canvasser_inst.id)

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCanvasserForm()

    return render(request, 'turfcutter/new_canvasser.html',
        {'form': form})


def new_canvas(request, campaign_id):

    if request.method == 'POST':
        form = NewCanvasForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # (here we just write it to the model due_back field)
            canvas_inst = form.save(commit=False)
            canvas_inst.owner = request.user
            canvas_inst.campaign = Campaign.objects.get(pk=campaign_id)
            canvas_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/turfcutter/canvas-area/%d/' %
                canvas_inst.id)

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCanvasForm()

    return render(request, 'turfcutter/new_canvas.html',
        {'form': form})


def index(request):
    return render(request, 'turfcutter/index.html',
        {'campaign_list': Campaign.objects.all()})


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
            return HttpResponseRedirect('/turfcutter/campaigns/')

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCampaignForm()

    return render(request, 'turfcutter/new_campaign.html',
        {'form': form})


def campaign_details(request, campaign_id):
    this_campaign = get_object_or_404(Campaign, id=campaign_id)
    canvas_list = Canvas.objects.filter(campaign_id=campaign_id)
    return render(request, 'turfcutter/campaign_details.html',
        {'campaign': this_campaign, 'canvas_list': canvas_list})


def canvas_details(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_turfs = Turf.objects.filter(canvas_id=canvas_id)
    turf_info = {}
    for turf in these_turfs:
        these_parcels = Parcel.objects\
            .filter(centroid__within=turf.geom)\
            .order_by('prop_street', 'prop_street_num')
        this_info = {'turf': turf, 'parcels': these_parcels}
        turf_info[turf.id] = this_info
    return render(request, 'turfcutter/canvas_details.html',
        {'canvas': this_canvas, 'canvas_area': this_canvas_area,
        'turf_info_dict': turf_info})


def canvas_pdf(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_turfs = Turf.objects.filter(canvas_id=canvas_id)

    turf_info = []
    for turf in these_turfs:
        these_parcels = Parcel.objects.filter(centroid__within=turf.geom).order_by('prop_street', 'prop_street_num')
        this_info = {'turf': turf, 'parcels': these_parcels}
        turf_info.append(this_info)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="canvas-%d.pdf"' % canvas_id

    doc = SimpleDocTemplate(response)
    contents = []
    style = TableStyle([('INNERGRID', (0, 2), (-1,-1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 0), (-1, 1), 1.0, colors.black),
        ('LINEAFTER', (0, 1), (1, 1), 0.25, colors.black),
        ('LINEAFTER', (4, 1), (4, 1), 0.25, colors.black),
        ])

    for info in turf_info:
        canvassers = info['turf'].canvassers.all()
        canvasser_row = ', '.join(['%s %s' % (c.first_name, c.last_name) for c in canvassers])
        canvasser_header = [canvasser_row, '', '', '', '', '']
        header = ['Address', 'Home?', 'Response', '', '', 'Notes']
        parcel_table = [canvasser_header, header]

        for parcel in info['parcels']:
            apt_num = '' if parcel.unit_apt_num is None else parcel.unit_apt_num
            parcel_address = '%s %s' % (parcel.prop_street_num, parcel.prop_street)
            parcel_table.append([parcel_address, '', 1, 2, 3, ' '*40])

        t = Table(parcel_table, colWidths=[150, 45, 20, 20, 20, 300], repeatRows=2)
        t.setStyle(style)
        contents.append(t)
        contents.append(PageBreak())

    doc.build(contents)

    return response

def canvasser_details(request, canvasser_id):
    this_canvasser = get_object_or_404(Canvasser, id=canvasser_id)
    return render(request, 'turfcutter/canvasser_details.html',
        {'canvasser': this_canvasser})


def canvas_area_define(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    if request.method == 'POST':
        form = CanvasAreaForm(request.POST)
        if form.is_valid():
            canvas_area = form.save(commit=False)
            canvas_area.canvas_id = canvas_id
            canvas_area.save()
            return HttpResponseRedirect('/turfcutter/turf/%d/' % canvas_id)
    else:
        form = CanvasAreaForm()
    return render(request, 'turfcutter/canvas_area.html', {'form': form})


def turf_define(request, canvas_id):
    this_canvas_area = get_object_or_404(CanvasArea, canvas_id=canvas_id)
    these_parcels = Parcel.objects\
        .filter(centroid__within=this_canvas_area.geom)
    these_turfs = Turf.objects.filter(canvas_id=canvas_id)
    turf_numbers = [int(t.name) for t in these_turfs]
    max_number = max(turf_numbers) if len(turf_numbers) > 0 else 0
    if request.method == 'POST':
        form = TurfForm(request.POST)
        if form.is_valid():
            turf = form.save(commit=False)
            turf.canvas_id = canvas_id
            turf.name = str(max_number + 1)
            turf.save()
            form.save_m2m()
            return HttpResponseRedirect('/turfcutter/turf/%d/' % canvas_id)
    else:
        form = TurfForm()
    return render(request, 'turfcutter/turf.html',
            {'form': form,
            'canvas_area': this_canvas_area,
            'canvas_id': canvas_id,
            'parcels': these_parcels,
            'turfs': these_turfs})


def turf_select(request, canvas_id):
    this_canvas = get_object_or_404(Canvas, id=canvas_id)
    these_turfs = Turf.objects.filter(canvas_id=canvas_id).order_by('name')
    return render(request, 'turfcutter/turf_selection.html',
        {'turf_list': these_turfs, 'canvas': this_canvas})


def turf_canvas(request, turf_id):
    this_turf = get_object_or_404(Turf, id=turf_id)
    this_canvas = Turf.canvas
    these_parcels = Parcel.objects.filter(
        centroid__within=turf.geom).order_by('prop_street', 'prop_street_num')
    return render(request, 'turfcutter/turf_canvas.html',
        {'turf': this_turf, 'canvas': this_canvas,
        'parcel_list': these_parcels})


def new_interaction(request, turf_id, parcel_id):
    this_turf = get_object_or_404(Turf, id=turf_id)
    this_parcel = get_object_or_404(Parcel, id=parcel_id)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.turf = this_turf
            interaction.parcel = this_parcel
            interaction.save()
            return HttpResponseRedirect('/turfcutter/turf-canvas/%d/' % turf_id)
    else:
        form = InteractionForm()
    return render(request, 'turfcutter/interaction.html',
            {'form': form})
