from django.urls import path
from app5.views import users_view,rounds_view,join_view, registered,roundscomple,userview,roundview,joinview

urlpatterns = [
    path("users/",users_view),
    path("registered_users/", registered),
    path("rounds/",rounds_view),
    path("roundsinfor/",roundscomple),
    path("joined/",join_view),
    path("usersformed/",userview),
    path("roundsformed/",roundview),
    path("joinformed/",joinview)
]
