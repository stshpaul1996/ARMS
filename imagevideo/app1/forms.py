from django.forms import ModelForm
from .models import Cricketer
from django import forms

class CricketerModelForm(forms.ModelForm):
    class Meta():
        model = Cricketer
        fields = '__all__'
