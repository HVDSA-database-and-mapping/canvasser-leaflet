from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import *
from djgeojson.views import TiledGeoJSONLayerView
from django.contrib.gis.db.models.functions import AsGeoJSON, Transform
from django.forms import modelformset_factory

import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .forms import *


class UntrimmedTiledGeoJSONLayerView(TiledGeoJSONLayerView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trim_to_boundary = False


class CanvassListView(generic.ListView):
    model = Canvass


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


def new_canvass(request, campaign_id):

    if request.method == 'POST':
        form = NewCanvassForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # (here we just write it to the model due_back field)
            canvass_inst = form.save(commit=False)
            canvass_inst.owner = request.user
            canvass_inst.campaign = Campaign.objects.get(pk=campaign_id)
            canvass_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/turfcutter/canvass-area/%d/' %
                canvass_inst.id)

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCanvassForm()

    return render(request, 'turfcutter/new_canvass.html',
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
    canvass_list = Canvass.objects.filter(campaign_id=campaign_id).order_by('date')
    return render(request, 'turfcutter/campaign_details.html',
        {'campaign': this_campaign, 'canvass_list': canvass_list})


def canvass_details(request, canvass_id):
    this_canvass = get_object_or_404(Canvass, id=canvass_id)
    this_canvass_area = get_object_or_404(CanvassArea, canvass_id=canvass_id)
    these_turfs = Turf.objects.filter(canvass_id=canvass_id).order_by('name')
    turf_info = {}
    for turf in these_turfs:
        these_parcels = Parcel.objects\
            .filter(centroid__within=turf.geom)\
            .order_by('prop_street', 'prop_street_num')
        this_info = {'turf': turf, 'parcels': these_parcels}
        turf_info[turf.id] = this_info
    return render(request, 'turfcutter/canvass_details.html',
        {'canvass': this_canvass, 'canvass_area': this_canvass_area,
        'turf_info_dict': turf_info})


def canvass_pdf(request, canvass_id):
    this_canvass = get_object_or_404(Canvass, id=canvass_id)
    this_canvass_area = get_object_or_404(CanvassArea, canvass_id=canvass_id)
    these_turfs = Turf.objects.filter(canvass_id=canvass_id)

    turf_info = []
    for turf in these_turfs:
        these_parcels = Parcel.objects.filter(
            centroid__within=turf.geom).order_by(
            'prop_street', 'prop_street_num')
        this_info = {'turf': turf, 'parcels': these_parcels}
        turf_info.append(this_info)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
        'attachment; filename="canvass-%d.pdf"' % canvass_id

    font_file = '/home/rwturner/django-apps/hvdsa/turfcutter/static/Symbola_hint.ttf'
    symbola_font = TTFont('Symbola', font_file)
    pdfmetrics.registerFont(symbola_font)

    doc = SimpleDocTemplate(response)
    contents = []
    style = TableStyle([('INNERGRID', (0, 3), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEBELOW', (0, 1), (-1, 1), 0.25, colors.black),
        ('LINEBELOW', (0, 2), (-1, 2), 1.0, colors.black),
        ('LINEAFTER', (0, 2), (2, 2), 0.25, colors.black),
        ('LINEAFTER', (5, 2), (5, 2), 0.25, colors.black),
        ('FONT', (0, 0), (-1, -1), 'Symbola'),
        ('FONTSIZE', (0, 0), (0, 0), 16)
    ])

    for info in turf_info:
        turfname_row = ['Turf %s' % info['turf'].name, '', '', '', '', '', '']
        header_buffer = [''] * len(turfname_row)
        header = ['Address', 'Home?', 'Accept?', 'Response', '', '', 'Notes']
        parcel_table = [turfname_row, header_buffer, header]

        for parcel in info['parcels']:
            apt_num = '' if parcel.unit_apt_num is None else parcel.unit_apt_num
            parcel_address = '%s %s' % (parcel.prop_street_num, parcel.prop_street)
            parcel_table.append([parcel_address, '', '', '\u263A', u"\U0001F610", '\u2639', ' ' * 40])

        t = Table(parcel_table, colWidths=[150, 45, 45, 20, 20, 20, 265], repeatRows=2)
        t.setStyle(style)
        contents.append(t)
        contents.append(PageBreak())

    doc.build(contents)

    return response


def canvasser_details(request, canvasser_id):
    this_canvasser = get_object_or_404(Canvasser, id=canvasser_id)
    return render(request, 'turfcutter/canvasser_details.html',
        {'canvasser': this_canvasser})


def canvass_area_define(request, canvass_id):
    this_canvass = get_object_or_404(Canvass, id=canvass_id)
    if request.method == 'POST':
        form = CanvassAreaForm(request.POST)
        if form.is_valid():
            canvass_area = form.save(commit=False)
            canvass_area.canvass_id = canvass_id
            canvass_area.save()
            return HttpResponseRedirect('/turfcutter/turf/%d/' % canvass_id)
    else:
        form = CanvassAreaForm()
    return render(request, 'turfcutter/canvass_area.html', {'form': form})


def turf_define(request, canvass_id):
    this_canvass_area = get_object_or_404(CanvassArea, canvass_id=canvass_id)
    these_parcels = Parcel.objects\
        .filter(centroid__within=this_canvass_area.geom)
    these_turfs = Turf.objects.filter(canvass_id=canvass_id)
    turf_numbers = [int(t.name) for t in these_turfs]
    max_number = max(turf_numbers) if len(turf_numbers) > 0 else 0
    if request.method == 'POST':
        form = TurfForm(request.POST)
        if form.is_valid():
            turf = form.save(commit=False)
            turf.canvass_id = canvass_id
            turf.name = str(max_number + 1)
            turf.save()
            form.save_m2m()
            return HttpResponseRedirect('/turfcutter/turf/%d/' % canvass_id)
    else:
        form = TurfForm()
    return render(request, 'turfcutter/turf.html',
            {'form': form,
            'canvass_area': this_canvass_area,
            'canvass_id': canvass_id,
            'parcels': these_parcels,
            'turfs': these_turfs})


def turf_select(request, canvass_id):
    this_canvass = get_object_or_404(Canvass, id=canvass_id)
    these_turfs = Turf.objects.filter(canvass_id=canvass_id).order_by('name')
    return render(request, 'turfcutter/turf_selection.html',
        {'turf_list': these_turfs, 'canvass': this_canvass})


def turf_canvass(request, turf_id):
    this_turf = get_object_or_404(Turf, id=turf_id)
    this_canvass = Turf.canvass
    these_parcels = Parcel.objects\
        .filter(centroid__within=this_turf.geom)\
        .order_by('prop_street', 'prop_street_num')
    return render(request, 'turfcutter/turf_canvass.html',
        {'turf': this_turf, 'canvass': this_canvass,
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
            return HttpResponseRedirect(
                '/turfcutter/turf-canvass/%d/' % turf_id)
    else:
        form = InteractionForm()
    return render(request, 'turfcutter/interaction.html',
            {'form': form, 'parcel': this_parcel})

def turf_interactions(request, turf_id):
    this_turf = get_object_or_404(Turf, id=turf_id)
    InteractionFormSet = modelformset_factory(Interaction, form=InlineInteractionForm)
    if request.method == 'POST':
        this_formset = InteractionFormSet(queryset=Interaction.objects.filter(turf=turf_id), data=request.POST)
        if this_formset.is_valid():
            this_formset.save()
    else:
        this_formset = InteractionFormSet(queryset=Interaction.objects.filter(turf=turf_id))
    return render(request, 'turfcutter/turf_interactions.html', {'formset': this_formset, 'turf': this_turf})

