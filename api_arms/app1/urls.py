from django.urls import path
from .views import SampleView, CustomerView, OrdersView

urlpatterns = [
   path("", SampleView.as_view()),
   path("register/", CustomerView.as_view()),
   path("users/", CustomerView.as_view()),
   path("users/<int:pk>/", CustomerView.as_view()),
   path("users/orders/", OrdersView.as_view()),
  

]
