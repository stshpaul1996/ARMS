from django.shortcuts import render
from .forms import MediaForm

from .models import MediaDB
# Create your views here.

def media_view(request):
    form = MediaForm()
    if request.method == "POST":
        print("possss")
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid:
            #print("data", form)
            form.save()
            data = MediaDB.objects.all()
            form = MediaForm()
            return render(request, "load.html", {"data": data, "form": form}) 
        
    return render(request, "image.html", {"form":form})
