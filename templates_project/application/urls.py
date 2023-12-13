from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_view),
    path("animal/",views.animal_view),
    path("hi/",views.hi_nanna_view),
    path("kota/",views.kotabomalli_view),
    path("extra/",views.extra_view),
]
