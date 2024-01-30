from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('category/',views.CategoryView.as_view()),
    path('category/<int:pk>/',views.CategoryView.as_view()),
    path('product/',views.ProductView.as_view()),
    path('product/<int:pk>/',views.ProductView.as_view()),
    path('purchase/',views.Purchase.as_view()),
    path('purchase/<int:pk>/',views.Purchase.as_view()),
    path('sales/',views.Sale.as_view()),
    path('sales/<int:pk>/',views.Sale.as_view()),
    path('stock/<int:id>/',views.StockView.as_view()),
]