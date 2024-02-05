from django.urls import path
from . import views
urlpatterns = [
    path('category/',views.CategoryView.as_view()),
    path('category/<int:pk>/',views.CategoryView.as_view()),
    path('product/',views.ProductView.as_view()),
    path('product/<int:pk>/',views.ProductView.as_view()),
    path('purchase/',views.PurchaseView.as_view()),
    path('sales/',views.SalesView.as_view()),
    path('stock/',views.StockView.as_view()),
]