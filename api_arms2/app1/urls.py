from django.urls import path, include
from app1.views import ProductV, OpeningStockV

urlpatterns = [
    
    path('product/',ProductV.as_view()),
    path('opening/',OpeningStockV.as_view()),
]