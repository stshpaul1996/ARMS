from django import forms
from . models import Aspirant

class AspirantForm(forms.ModelForm):
    class Meta:
        model = Aspirant
        fields = "__all__"
        