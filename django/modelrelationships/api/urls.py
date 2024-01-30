from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('category/',views.CategoryView.as_view()),
    path('category/<int:pk>/',views.CategoryView.as_view()),
    path('salesorder/',views.SalesOrderView.as_view()),
    path('salesorder/<int:pk>/',views.SalesOrderView.as_view()),
    path('purchaseorder/',views.PurchaseOrderView.as_view()),
    path('purchaseorder/<int:pk>/',views.PurchaseOrderView.as_view()),
    path('product/',views.ProductView.as_view()),
    path('product/<int:pk>/',views.ProductView.as_view()),
    # path('stock/<int:pk>/',views.StockView)
]