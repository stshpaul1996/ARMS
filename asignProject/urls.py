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
from django.urls import path
from project import views
import psutil
from django.http import HttpResponse
from project import own_views
from project_arms import own_view

def get_ram(request):
    ram_size = psutil.virtual_memory().total
    return HttpResponse(ram_size)

    
urlpatterns = [
    path("admin/", admin.site.urls),
    path("ram/", get_ram),
    
    path("os/",views.get_os),
    path("ncores/",own_views.get_ncores),
    path("html/",own_view.get_html),
    path("svar/",views.s_var),
    path("pvar/",views.p_var),
]
