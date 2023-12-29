from django import forms
from . models import Medias

class MediasForm(forms.ModelForm):
    class Meta:
        model=Medias
        fields="__all__"
