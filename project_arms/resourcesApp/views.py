from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Resources, Rounds
from .forms import ResourcesForm, RoundsForm

# Create your views here.
def resources_view(request):
    return render(request,"resources/header.html")

def form_view(request):
    resource = ResourcesForm()
    if request.method == 'GET':
        return render(request, "resources/register.html", {"resource":resource})
    else:
        post = ResourcesForm(request.POST)
        if post.is_valid():
            post.save()
            return render(request, "resources/success.html")
       
        
def users_view(request):
    db_data = Resources.objects.all()
    return render(request, "resources/users.html", {"content":db_data})


def update_candidate(request, id):
   
    get_data = Resources.objects.get(id=id)
    form = ResourcesForm(instance=get_data)
    msg = f'You have successfully updated with {get_data.first_name} {get_data.last_name}'
    if request.method == 'POST':
        form = ResourcesForm(request.POST, instance=get_data)
        content= Resources.objects.all()
        if form.is_valid():
            form.save()
            return redirect("/resources/registered_candidates/")
        

    return render(request, "resources/update.html", {'form':form})
        

def delete_candidate(request, id):
    get_data = Resources.objects.get(id=id)
    get_data.delete()
    db_data = Resources.objects.all()
    # return render(request, "resources/users.html", {"content":db_data})
    return render(request, "resources/delete.html", {'id':id})

def rounds_form(request):
    formRounds = RoundsForm()
    if request.method == "POST":
        if formRounds.is_valid():
                formRounds = RoundsForm(request.POST)
                formRounds.save()
                return redirect("/resources/registered_candidates/")
    return render(request, "resources/rounds.html", {"formRounds":formRounds})

def table_view(request, id):
    user = Resources.objects.get(pk=id)  # Retrieve specific author by ID
    # Retrieve books written by the specific author
    round = Rounds.objects.filter(id=user)

    return render(request, 'resources/user_round.html', {'user': user, 'round': round})