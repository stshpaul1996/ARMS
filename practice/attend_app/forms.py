from django import forms
from .models import EmployeeInfo

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=EmployeeInfo
        fields='__all__'