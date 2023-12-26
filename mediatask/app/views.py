from django.shortcuts import render
from app.models import Media
from app.forms import MediaForm

# Create your views here.
def mediaview(request):
    form=MediaForm()
    if request.method=="POST":
        form=MediaForm(data=request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            data=Media.objects.all()
            form=MediaForm()
            return render(request,"app/cricketer.html", {"data":data,"form":form})
    return render(request, "app/cricketer.html", {"form":form} )