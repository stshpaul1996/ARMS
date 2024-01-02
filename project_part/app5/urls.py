from django.urls import path
from app5.views import users_view,rounds_view,join_view, registered,roundscomple,userview,roundview,joinview,joincomple,base,update_view, delete_view

urlpatterns = [
    path("users/",users_view),
    path("registered_users/", registered, name="after_delete_registered"),
    path("rounds/",rounds_view),
    path("roundsinfor/",roundscomple),
    path("joined/",join_view),
    path("usersformed/",userview),
    path("roundsformed/",roundview),
    path("joinformed/",joinview),
    path("joincomplete/",joincomple),
    path("",base),
    path("update/<id>",update_view,name="user_update"),
    path("delete/<id>", delete_view, name="delete_update")
]
