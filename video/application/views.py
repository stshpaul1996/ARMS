from django.shortcuts import render,redirect
from .forms import MediasForm
from .models import Medias
# Create your views here.
def uploading(request):
    form=MediasForm()
    if request.method == 'POST':
        form=MediasForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/lists/")
    else:
        form=MediasForm()
    return render(request,"application/upload.html",{"form":form})

def listing(request):
    data=Medias.objects.all()
    return render(request,"application/lists.html",{"data":data})