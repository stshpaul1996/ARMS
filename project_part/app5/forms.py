from django.forms import ModelForm
from app5.models import Users,Rounds,Joined

class Usersform(ModelForm):
    class Meta:
        model=Users
        exclude=["pf"]
        #fields="__all__"
    def clean_first_name(self):
        return self.cleaned_data.get("first_name").upper()
class Roundsform(ModelForm):
    class Meta:
        model=Rounds
        fields="__all__"
class Joinedform(ModelForm):
    class Meta:
        model=Joined
        fields="__all__"