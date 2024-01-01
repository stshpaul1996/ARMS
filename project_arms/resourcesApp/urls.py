from django.urls import path

from .views import resources_view, form_view, users_view, update_candidate, delete_candidate, rounds_form,  table_view, resourecs_all

urlpatterns = [
    path("", resources_view),
    path("register/", form_view),
    path("registered_candidates/", users_view),
    path("update/<id>", update_candidate, name="update_candidate"),
    path("delete/<id>", delete_candidate, name="delete_candidate"),
    path("rounds/", rounds_form),
    path("user_round/<id>", table_view),
    path("all/", resourecs_all)

]