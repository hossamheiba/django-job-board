from django import forms
from .models import Applay

class Applay_form(forms.ModelForm):
    class Meta :
        model=Applay
        fields="__all__"