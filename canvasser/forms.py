from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from .models import Canvas, CanvasArea, CanvasSector


class NewCanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = '__all__'


class CanvasAreaForm(ModelForm):
    class Meta:
        model = CanvasArea
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}


class CanvasSectorForm(ModelForm):
    class Meta:
        model = CanvasSector
        fields = ('geom',)
        widgets = {'geom': LeafletWidget()}

