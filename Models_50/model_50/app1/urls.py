from django.urls import path
from . import views
urlpatterns = [
    path('product_details', views.Product_detail),
]