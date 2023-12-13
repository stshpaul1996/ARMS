
from django.urls import path
from App1.views import nithisha_view,kalkuri_view,parasa_view,kspaul_view,haritha_view,home

urlpatterns = [
    path("",home),
    path("nithisha",nithisha_view),
    path("kalkuri",kalkuri_view),
    path("parasa",parasa_view),
    path("satish",kspaul_view),
    path("haritha",haritha_view),

]