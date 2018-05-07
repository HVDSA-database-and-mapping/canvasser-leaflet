from django import forms

class NewCanvasForm(forms.Form):
    new_canvas_name = forms.CharField(label='Name your new canvas', max_length=140)

