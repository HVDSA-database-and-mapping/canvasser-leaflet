from django import forms
from django.forms import ModelForm, formset_factory
from leaflet.forms.widgets import LeafletWidget
from .models import *


# https://stackoverflow.com/a/44224563
class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'turfcutter/horizontal_select.html'


class DateInput(forms.DateInput):
    input_type = 'date'


class NewCampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'start_date', 'end_date']
        widgets = {'start_date': DateInput(), 'end_date': DateInput()}


class NewCanvassForm(ModelForm):
    class Meta:
        model = Canvass
        fields = ['name', 'date']
        widgets = {
            'date': DateInput()
        }


class NewCanvasserForm(ModelForm):
    class Meta:
        model = Canvasser
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class CanvassAreaForm(ModelForm):
    class Meta:
        model = CanvassArea
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}


class TurfForm(ModelForm):
    class Meta:
        model = Turf
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}


class InteractionForm(ModelForm):
    class Meta:
        model = Interaction
        fields = ('at_home', 'accepted_material', 'campaign_response',
            'dsa_response', 'notes')
        widgets = {'at_home': HorizontalRadioSelect, 'accepted_material': HorizontalRadioSelect,
                'campaign_response': HorizontalRadioSelect, 'dsa_response': HorizontalRadioSelect}
        labels= {'at_home': 'Home', 'accepted_material': 'Accept', 'campaign_response': 'Campaign', 'dsa_response': 'DSA'}

class InlineInteractionForm(ModelForm):
    class Meta:
        model = Interaction
        fields = ('at_home', 'accepted_material', 'campaign_response',
            'dsa_response', 'notes')
        widgets = {'at_home': HorizontalRadioSelect, 'accepted_material': HorizontalRadioSelect,
                'campaign_response': HorizontalRadioSelect, 'dsa_response': HorizontalRadioSelect,
                'notes': forms.Textarea(attrs={'rows': 1})}
        labels= {'at_home': 'Home', 'accepted_material': 'Accept', 'campaign_response': 'Campaign', 'dsa_response': 'DSA'}

