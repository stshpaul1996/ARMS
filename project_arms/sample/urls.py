
from django.urls import path
from sample.views import person1_create_view
urlpatterns = [
   
path("person1/create/", person1_create_view),# sample
   
]
