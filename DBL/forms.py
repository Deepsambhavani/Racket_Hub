from django import forms
from .models import rackets

class racketform(forms.Form):
    racket_type = forms.ModelChoiceField(queryset=rackets.objects.all(),label='select racket type')