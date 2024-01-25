from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CategoryV.as_view()), 
    path('pro/', Productv.as_view()),
    path('op/',OpeningStockV.as_view()),
    path('sale/',Salesv.as_view()),
    path('pur/',Purchasev.as_view()),
    path('stock/',Stockv.as_view()),
    path('stock/<int:id>/', Stockvp.as_view())
]