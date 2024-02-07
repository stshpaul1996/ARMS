
from django.urls import path
from .views import *


urlpatterns = [
   
    path("category/",  CategoryView.as_view()),
    path("category/<int:id>/",  CategoryView.as_view()),
    path("product/", ProductView.as_view()),
    path("product/<int:id>/", ProductView.as_view()),
    path("purchase/", PurchaseView.as_view()),
    path("purchase/<int:id>/", PurchaseView.as_view()),
    path("sales/", SalesView.as_view()),
    path("sales/<int:id>/", SalesView.as_view()),
    path("stock/", StockView.as_view()),
    path("stock/<int:id>/", StockView.as_view()),
]