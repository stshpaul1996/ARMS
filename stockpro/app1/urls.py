from django.urls import path
from .views import *

urlpatterns = [
    path("cat/", CategoryView.as_view()),
    path("pro/", ProductView.as_view()),
    path("pur/", PurchaseView.as_view()),
    path("sale/", SaleView.as_view()),
    path("stock/", StockView.as_view()),
]

'''

{
    "name": "milk",
    "unique_num":1001,
    "category":3,
    "cost":50.45,
    "stock":55

}

'''
