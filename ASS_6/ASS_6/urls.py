"""
URL configuration for ASS_6 project.

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
from testapp.views import machine_name
from testapp.own_views import no_of_cores
from own_views import temp_fun

from django.http import HttpResponse

from psutil import virtual_memory

memory_info = virtual_memory()

def v1(request):
    total_mem = memory_info.total/(1024**2)
    avail_mem = memory_info.available/(1024**2)

    return HttpResponse('total_memory is :{}  , available_memory :{}'.format(total_mem,avail_mem))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ram/', v1),
     path('os/', machine_name),
     path('ncores/',no_of_cores),
     path('users',temp_fun)
]
