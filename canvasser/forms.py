from django import forms
from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from .models import Canvas, CanvasArea, CanvasSector


class DateInput(forms.DateInput):
    input_type='date'

class NewCanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name', 'date', 'description']
        widgets = {
            'date': DateInput()
        }


class CanvasAreaForm(ModelForm):
    class Meta:
        model = CanvasArea
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}


class CanvasSectorForm(ModelForm):
    class Meta:
        model = CanvasSector
        fields = ('geom', 'canvassers')
        widgets = {'geom': LeafletWidget()}

