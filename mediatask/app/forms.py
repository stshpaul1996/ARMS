from django import forms
from app.models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model=Media
        fields='__all__'
