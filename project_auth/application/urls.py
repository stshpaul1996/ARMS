from django.urls import path
from . import views
urlpatterns = [
    path('',views.base_view),
    path('person/',views.person_view_create),
    path('login/',views.login_view),
    path('logout/',views.logout_view)
]