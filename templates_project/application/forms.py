from django import forms
from . models import display

class displayform(forms.ModelForm):
    class Meta:
        model=display
        fields="__all__"
    
    def clean_name(self):
        return self.cleaned_data.get("name").upper()
    
