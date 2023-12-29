
from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_item_view),
    path('dis/',views.display_item_view)
]