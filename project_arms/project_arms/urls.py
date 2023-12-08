"""
URL configuration for project_arms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse

import os
import psutil
import math
import platform
import multiprocessing

def per_env_var(request):
    res = os.environ.get("var")

    return HttpResponse(res)

def ses_env_var(request):
    os.environ["ses_var"] = "Hello Session Variable"
    return HttpResponse(os.environ.get("ses_var")) 

def set_env(request):
    os.environ["ses_var"] = "Hello Session Variable"
    return HttpResponse(os.environ.get("ses_var"))

def get_env(request):
   
    return HttpResponse(os.environ.get("ses_var"))

def get_ram(request):
    ram = psutil.virtual_memory().total
    gb = math.ceil(ram/(1024**3))
    ram_gb = f"{gb}GB RAM"
    return HttpResponse(ram_gb)

def get_os(request):
    
    return HttpResponse(platform.system())

def get_cores(request):
    return HttpResponse(multiprocessing.cpu_count())

def get_users(request):
    return HttpResponse("<h1>Hello Samba!</h1>")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pern", per_env_var),
    path("sess", ses_env_var),
    path("set/", set_env),
    path("get/", get_env),
    path("ram/", get_ram),
    path("os/", get_os),
    path("cores", get_cores),
    path("user/", get_users),
    path("resources/", include("resourcesApp.urls"))

]