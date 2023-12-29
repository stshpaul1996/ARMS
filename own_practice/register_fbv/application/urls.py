from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add/',views.adding),
    path('dis/',views.display),
    path('thank/',views.thank,name="thank"),
    path('logout/', views.logout_view,),
    path('signup/',views.signup_view),
    path('delete/<int:id>/',views.delete_view),
    path('update/<int:id>/',views.update_view),
]