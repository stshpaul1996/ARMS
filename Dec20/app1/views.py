from django.shortcuts import render
from .forms import MediaForm
from .models import MediaDB
# Create your views here.

def media_view(request):
    form = MediaForm()
    if request.method == "POST":
        form = MediaForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            data = MediaDB.objects.all()
            form = MediaForm()
            return render(request, "app1/load.html", {"data": data, "form": form}) 
    return render(request, "app1/image.html", {"form":form})