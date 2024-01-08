from django.urls import path
from .views import ProductView, CategoryView


urlpatterns = [
    path("pro/", ProductView.as_view()),
    path("pro/<int:id>/", ProductView.as_view()),
    path("cat/", CategoryView.as_view())

]