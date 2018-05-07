from django.forms import ModelForm
from .models import Canvas


class NewCanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name', 'start_date', 'end_date']
