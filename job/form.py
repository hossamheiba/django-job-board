from django import forms
from .models import Applay,job

class Applay_form(forms.ModelForm):
    class Meta :
        model=Applay
        fields="__all__"
        exclude=("job",)

        
class add_job(forms.ModelForm):
    class Meta :
        model=job
        fields="__all__"
        exclude=("owner","slug",)
        