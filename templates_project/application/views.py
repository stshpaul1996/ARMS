from django.shortcuts import render,redirect
from . models import display
from . forms import displayform
# Create your views here.
def home_view(request):
    return render(request, 'application/home.html')

def animal_view(request):
    return render(request, 'application/animal.html')

def hi_nanna_view(request):
    return render(request, 'application/hi_nanna.html')

def kotabomalli_view(request):
    return render(request, 'application/kotabomalli.html')

def extra_view(request):
    return render(request, 'application/extra.html')

def movie(request):
    m=display.objects.all()
    return render(request,"application/movie.html",{"m":m})

def add_movie_view(request):
    message=""
    form=displayform()
    if request.method == "POST":
        form=displayform(request.POST)
        if form.is_valid():
            form.save()
            message = "user submitted"
            return redirect(movie)
        else:
            message = ""
        return render(movie)
    return render(request,"application/addmovie.html",{"message":message,"form":form})

# def add_movie_view(request):
#     message=""
#     if request.method == "POST":
#         data=request.POST
#         # print(data["movie_name"])
#         # print(data["image_path"])
#         d=display(name=data["name"],address=data["address"],image_path=data["image_path"])
#         d.save()
#         message = "user submitted"
#         return redirect(movie)
#     else:
#         message = ""
#     return render(request,"application/addmovie.html",{"message":message})