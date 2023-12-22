from django.urls import path
from .views import empdata,empdetail


urlpatterns=[
    path('emp/',empdata),
    path("ed/",empdetail),
    # path('attend/',attend)


]

