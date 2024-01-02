from django import forms

from .models import MediaDB

class MediaForm(forms.ModelForm):
    class Meta:
        model = MediaDB
        fields = "__all__"