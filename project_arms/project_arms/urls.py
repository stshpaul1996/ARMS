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
from django.http import HttpResponse
# def task1(p1):
#     print("*"*20)
#     print(p1)
#     # return "hello world"
#     # return HttpResponse("Hello world")
#     resp = """
#     <html>
#     <head> <title>SAMPLE</title> </head>
#     </html>
#     """
#     return HttpResponse(resp)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # path("users/", task1),#task1(request_obj)# server parsing that return value. expecting HttpReponse. 
]
