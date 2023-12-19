from django.forms import ModelForm
from django import forms
from app1.models import Aspirant

class AspirantModelForm(forms.ModelForm):
    class Meta:
        model = Aspirant
        exclude = ('application_no','timestamp')
