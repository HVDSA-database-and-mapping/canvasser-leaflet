from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Canvas, Canvasser
from djgeojson.views import TiledGeoJSONLayerView

import datetime

from .forms import NewCanvasForm


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
            canvas_inst = Canvas(name=form.cleaned_data['new_canvas_name'])
            canvas_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('canvases'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCanvasForm()

    return render(request, 'canvasser/index.html',
        {'form': form})