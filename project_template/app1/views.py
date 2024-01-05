from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Cricketers
from app1.forms import CricketerForm, CricketerModelForm
#from .constants import data

# Create your views here.
def cricketer_add_view(request):
    message = ""
    errors = ""
    if request.method == "POST":
        #data = request.POST
        # print(data['cricketer_name'])
        # print(data['cricketer_image_path'])
        # cricketer_inst = Cricketers(name=data['cricketer_name'], 
        # 
        #                             image_path=data['cricketer_image_path'])
        """
        cricketer_inst = Cricketers(name=data['name'], 
                                    image_path=data['image_path'])
        cricketer_inst.save()# this line insert data in to database
        message = "Cricketer created successfully"
        
        """
        form = CricketerModelForm(data=request.POST, files=request.FILES)
        #import pdb;pdb.set_trace()
        if form.is_valid():
            # it will call the validators of models
            form.save()
        else:
            errors = form.errors
            return render(request, "app1/add_cricketer.html", {"message": message, "form": form, "errors": errors})
        return redirect("/app1/cricketers/")
    else:
        message=""
        form = CricketerModelForm()
    return render(request, "app1/add_cricketer.html", {"message": message, "form": form})

def cricketers_view(request):
    data = Cricketers.objects.all()
    return render(request, "app1/cricketers.html", 
                  {"cricketers_data": data, "header": "LIST OF CRICKETERS"})

def cricketer_view_id(request, cricketer_id):
    import pdb;pdb.set_trace()
    type_data = str(type(cricketer_id))
    return HttpResponse("id"+str(cricketer_id))

def cricketer_view(request, cricketer):
    type_data = str(type(cricketer))
    return HttpResponse("name"+cricketer)


def home_view(request):
    return render(request, "app1/home.html")

def kohli_view(request):
    return render(request, "app1/kohli.html")
