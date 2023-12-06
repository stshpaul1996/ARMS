"""
URL configuration for ARGV project.

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
from app import views
import psutil
from app import own_views
from django.http import HttpResponse
from ARGV import views as p

def ram(request):
    ram = psutil.virtual_memory().total
    return HttpResponse(ram)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home', views.func),
    path('set', views.set_var),
    path('get', views.get_var),
    path('ram', ram),
    path('osname', views.os_name),
    path('cores', own_views.cores),
    path('html', p.html_fun)
]
