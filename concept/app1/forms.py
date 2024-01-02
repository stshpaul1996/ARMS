from django.forms import ModelForm
from django import forms
from app1.models import Aspirant,Rounds,OnBoarded

class AspirantModelForm(forms.ModelForm):
    class Meta:
        model = Aspirant
        exclude =('application_no','timestamp')

class RoundComForm(forms.ModelForm):
    class Meta:
        model = Rounds
        fields = ('marks_communication_test','isQualified_communication_test','feedback_communication_test')

class RoundTechForm(forms.ModelForm):
    class Meta:
        model = Rounds
        fields =('marks_technical_test','isQualified_technical_test','feedback_technical_test')

class RoundCEOForm(forms.ModelForm):
    class Meta:
        model = Rounds
        fields =('marks_CEO_test','isQualified_CEO_test','feedback_CEO_test')

class OnboaredForm(forms.ModelForm):
    class Meta:
        model = OnBoarded
        fields= '__all__'
