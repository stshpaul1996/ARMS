
from django.urls import path
from .views import display,show_cric
urlpatterns = [
    path('',display,name='home'),
    path('/show_cric',show_cric,name='show_cric')
]