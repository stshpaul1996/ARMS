from django import forms
from . models import Aspirant
from django.contrib.auth.models import User

class Aspirant_form(forms.ModelForm):
    class Meta:
        model = Aspirant
        fields="__all__"

    def clean(self):
        total_clean_data=super().clean()
        Post_Gradatio_year=total_clean_data["Post_Gradation_Passed_out_year"]
        if not (2016 <Post_Gradatio_year <2023):
            raise forms.ValidationError("Post_Gradation_Passed_out_year should be greater than 2016 and less than 2023")

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

#user name:bhagavaan
#password :python1234