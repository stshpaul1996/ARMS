from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Aspirant
from app1.forms import AspirantModelForm

# Create your views here.
def asp(request):
    
    message = ''
    if request.method == 'POST':
        data = request.POST
        message = 'The upload is sucessfull'
        form = AspirantModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = AspirantModelForm()
        else:
            message ='The upload is not sucessfull'
    else:
        form = AspirantModelForm()
        message = 'The upload is not sucessfull'
    return render(request,'app1/forms.html',{'message':message,'form':form})
                                 


def see(request):
    data = Aspirant.objects.all()
    return render(request,'app1/index.html',{'data1':data,})


