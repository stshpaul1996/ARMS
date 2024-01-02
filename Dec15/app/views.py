from django.shortcuts import render
from django.http import HttpResponse
from app.models import Users
def user_view(request): 
    if request.method=="POST":
        data=request.POST
        user_instance=Users(name=data['user_name'],email=data['email_id']).save()
        user = Users.objects.all()
        return render(request, "app/users.html",{"users":user})
    else:
        user = Users.objects.all()
        return render(request, "app/users.html", {"users":user})