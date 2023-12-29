from django.urls import path
from . views import SampleView
urlpatterns = [
    path("<int:id>/",SampleView.as_view()),
    path("",SampleView.as_view())
]