from django import forms
from .models import rackets, racket_type

class racketform(forms.Form):
    racket_type = forms.ModelChoiceField(queryset=racket_type.objects.all(), label='Select Brand')