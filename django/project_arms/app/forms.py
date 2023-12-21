from django import forms
from app.models import Aspirant

class AspirantForm(forms.ModelForm):
    def __init__(self, *args, exclude_fields=None, **kwargs):
        super().__init__(*args, **kwargs)
        if exclude_fields:
            for field_name in exclude_fields:
                if field_name in self.fields:
                    del self.fields[field_name]

    class Meta:
        model=Aspirant
        fields='__all__'
        