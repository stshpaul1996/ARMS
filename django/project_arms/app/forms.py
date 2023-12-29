from django import forms
from app.models import Aspirant,Rounds

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
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput( attrs={'class': 'form-control'}),
            'gradution':forms.Select(attrs={'class':'form-control'}),
            'post_gradution': forms.TextInput(attrs={'class':'form-control'}),
            'stream': forms.TextInput(attrs={'class': 'form-control'}),
            'passed_out_year': forms.NumberInput( attrs={'class': 'form-control'}),
            'trained_on_technology':forms.Select(attrs={'class':'form-control'}),
            'trained_institue': forms.TextInput(attrs={'class':'form-control'}),
            'duration_of_course': forms.NumberInput(attrs={'class': 'form-control'}),
            'reference_name': forms.TextInput( attrs={'class': 'form-control'}),
            'hear_about_interview':forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.Select(attrs={'class':'form-control'}),
            'Previous_company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'current_ctc': forms.NumberInput( attrs={'class': 'form-control'}),
            'expected_ctc':forms.NumberInput(attrs={'class':'form-control'}),
            'last_company': forms.TextInput(attrs={'class':'form-control'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'})
            
        }

class RoundForm(forms.ModelForm):
    class Meta:
        models=Rounds
        fields='__all__'
        