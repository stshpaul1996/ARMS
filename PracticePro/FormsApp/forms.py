from django import forms

from .models import Resources

class FormResources(forms.ModelForm):
    class Meta:
        model = Resources
        fields = "__all__"
        #exclude = ['created_at']
