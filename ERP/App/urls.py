
from django.urls import path
from .views import *

urlpatterns = [
    path("category/",CategoryView.as_view()),
     path("product/",ProductView.as_view()),
    path("sales/",SalesView.as_view()),
     path("purchase/",PurchaseView.as_view()),
    path("stock/",StockReportAllView.as_view()),
     path("stock/<int:id>",StockReportView.as_view())
]