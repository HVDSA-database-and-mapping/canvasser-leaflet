from django import forms


class NewCanvasForm(forms.Form):
    new_canvas_name = forms.CharField(label='new_canvas_form',
        max_length=140, help_text='140 characters max')

