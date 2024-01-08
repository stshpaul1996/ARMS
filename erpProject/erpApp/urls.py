
from django.urls import path
from erpApp.views import *

urlpatterns = [
    # path("person/<int:pk>/", SampleView.as_view()),
   # path("person/", SampleView.as_view()),
    path("product/", ProductView.as_view()),
     #path("salesorder/",SalesOrderView.as_view()),
    # path("purchaseorder/",PurchaseOrderView.as_view()),
     path("openingstock/",OpeningStockView.as_view()),
     path("sales/",ProductSalesView.as_view()),
     path("purchase/",ProductPurchaseView.as_view()),
     path("stock/<int:id>",StockView.as_view())
    # path("productcost/",ProductCostView.as_view()),
    # path("category/", CategoryView.as_view()),
    # path("product/<int:id>", ProductView.as_view()),
    # path("salesorder/<int:id>",SalesOrderView.as_view()),
    # path("purchaseorder/<int:id>",PurchaseOrderView.as_view()),
    # path("openingstock/<int:id>",OpeningStockView.as_view()),
    # path("productcost/<int:id>",ProductCostView.as_view()),
    # path("category/<int:id>", CategoryView.as_view()),
    
    
]