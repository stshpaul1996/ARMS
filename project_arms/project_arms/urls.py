"""project_arms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import os
from django.http import HttpResponse

def login(request):
    value=os.environ.get('variable')
    env="Permanant environment variable is:{}".format(value)
    return HttpResponse(env)

def set_session_environment(request):
    os.environ["session_variable"]="hello session variable"
    return HttpResponse(os.environ.get("session_variable"))

def get_session_environment(request):
    return HttpResponse(os.environ.get("session_variable"))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',login),
    path('session/',set_session_environment),
    path('get_session/',get_session_environment)
]
