# compiler/forms.py
from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea, label='Enter your code')
    language = forms.ChoiceField(choices=[('python', 'Python'), ('c', 'C'), ('cpp', 'C++')], label='Select Language')
