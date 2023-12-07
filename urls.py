"""
URL configuration for arms_project project.

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
from django.urls import path
import os
import psutil
from django.http import HttpResponse
from knownapp import views
#from knownapp import views

def permanent_env_variable(request):
    res=os.environ.get('var')
    return HttpResponse(res)
def session_env_variable(request):
    os.environ['session_variable']='This session variable'
    return HttpResponse(os.environ.get('session_variable'))
def set_env(request):
    os.environ['session_variable']='This is Session variable'
    return HttpResponse(os.environ.get('session_variable'))
def get_env(request):
    return HttpResponse(os.environ.get('sesion_variable'))

def size_ram(request):
    ram_info=psutil.virtual_memory()
    total_ram_size=ram_info.total//(1024**3)
    return HttpResponse(f"your os ram size is: {total_ram_size} GB")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('permanent/', permanent_env_variable ),
    path('session/', session_env_variable),
    path('set/', set_env),
    path('get/', get_env),
    path('size/', size_ram),
    path('os/',views.get_os_name),
    path('cores/',views.get_cores),
    path('code/',views.code),
]
