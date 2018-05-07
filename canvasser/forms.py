from django.forms import ModelForm


class NewCanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name', 'start_date', 'end_date']
