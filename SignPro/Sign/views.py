from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import requests

def perform_login(username="nithisha", password="nithisha"):
    login_url = 'http://localhost:8001/login/'  
    response = requests.post(login_url, data={'username': username, 'password': password})

    if response.status_code == 200:
        token = response.json().get('jwt_code')  
        return HttpResponse(token)
    else:
        return HttpResponse(response.status_code)



