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
from sample import views
from django.http import HttpResponse
import psutil
import multiprocessing
import platform


def ram(request):
    ram_info = psutil.virtual_memory()
    result = (
        f"Total: {ram_info.total / 1024 / 1024 / 1024:.2f} GB<br>"
        f"Available: {ram_info.available / 1024 / 1024 / 1024:.2f} GB<br>"
        f"Used: {ram_info.used / 1024 / 1024 / 1024:.2f} GB<br>"
        f"Percentage usage: {ram_info.percent}%"
    )

    return HttpResponse(result)
def os(request):
    result =(
        f"The name of os is {platform.system()}<br>"
        f"The version is {platform.version()}"
    )
    return HttpResponse(result)

def ncores(request):
    result = (
        f"The number of the cores in this machine are {multiprocessing.cpu_count()}"
    )
    return HttpResponse(result)

def users(request):
    html_code = """
    <html>
            <head>
                <title>
                    User Page
                </title>
            </head>
            <body>
                <h1>This is a User page</h1>
                <pr>Welcome to this page. This is Thatipamula Vamshi</Pr>
            <body>
    </html>  
    """
    return HttpResponse(html_code)

#print(dir(os.environ))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stupid/',views.hello),
    path('tejus/',views.login, name = 'hello1'),
    path('ram/',ram),
    path('os/',os),
    path('ncores/',ncores),
    path('users/',users),
 ]
