"""
URL configuration for jwtAuth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from testapp.views import ProductView,CategoryView,Purchase,Sale,StockReportOfsingleObject,StockReportS,LoginView,GetCredentials

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product', ProductView.as_view()),
        path('product/<int:pk>', ProductView.as_view()),
         path('purchase', Purchase.as_view()),
         path('sale', Sale.as_view()),
         path('stockreports', StockReportS.as_view()),
          path('stockreport/<int:id>', StockReportOfsingleObject.as_view()),
    path('category',CategoryView.as_view()),
    path('login',LoginView.as_view()),
    path("getcredentials",GetCredentials.as_view())
]