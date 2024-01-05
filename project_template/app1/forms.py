from app1.models import Cricketers
from django import forms 
class CricketerForm(forms.Form):
    name = forms.CharField(max_length=250)
    image_path = forms.CharField(max_length=250)

class CricketerModelForm(forms.ModelForm):
    # def clean_name(value):
    #     return value.upper()

    class Meta:
        model = Cricketers
        #fields = ("name", "image_path")  #"__all__"
        exclude = ("created_date",)


    def clean_name(self):

        return self.cleaned_data.get("name").upper()
        
    # def clean_image_path(self):

    #     return self.cleaned_data.get("image_path").lower()
       

    # def clean(self):
    #     print("form clean")
    #     import pdb;pdb.set_trace()
    #     return None




