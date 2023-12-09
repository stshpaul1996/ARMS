
from django.urls import path
from base.views import base_customer_create_view
urlpatterns = [
   
    path("customer/create/", base_customer_create_view),# base
   
]
