from django.urls import path
from app1 import views

urlpatterns = [
    
    path('home/',views.Home),
    path('list/',views.List, name = 'list'),
    path('round1/',views.Communication),
    path('round2/',views.Technical),
    path('round3/',views.CEO),
    
]
