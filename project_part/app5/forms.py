from django.forms import ModelForm
from app5.models import Users,Rounds,Joined

class Usersform(ModelForm):
    class Meta:
        model=Users
        exclude=["pf"]
        #fields="__all__"
class Roundsform(ModelForm):
    class Meta:
        model=Rounds
        fields="__all__"
class Joinedform(ModelForm):
    class Meta:
        model=Joined
        fields="__all__"
                
                