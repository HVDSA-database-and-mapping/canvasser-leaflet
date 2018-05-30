from django import forms
from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class NewCampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'start_date', 'end_date', 'description']
        widgets = {'start_date': DateInput(), 'end_date': DateInput()}


class NewCanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name', 'date', 'description', 'campaign']
        widgets = {
            'date': DateInput()
        }

class NewCanvasserForm(ModelForm):
    class Meta:
        model = Canvasser
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class CanvasAreaForm(ModelForm):
    class Meta:
        model = CanvasArea
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}


class TurfForm(ModelForm):
    class Meta:
        model = Turf
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}

