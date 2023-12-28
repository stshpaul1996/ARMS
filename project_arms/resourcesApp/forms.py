from django import forms
from .models import Resources, Rounds, OnBoarded

class ResourcesForm(forms.ModelForm):
    class Meta:
        model= Resources
        exclude = ["created_at"]

    def clean(self):
        cleaned_data = super().clean()
        for key,value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.upper()
        return cleaned_data
    

class RoundsForm(forms.ModelForm):
    class Meta:
        model= Rounds
        fields = "__all__"
    