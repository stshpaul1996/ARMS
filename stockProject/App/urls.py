from django.urls import path
from .views import *
from .viewsets import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
#router.register(r'viewset_person', PersonModelViewset, basename='viewset_person')
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleModelViewset, basename='role')
#router.register(r'api', PersonModelViewset, basename='api')
#router.register(r'permission', PersonModelViewset, basename='permission')


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
   # path('login',LoginView.as_view()),
   # path("getcredentials",GetCredentials.as_view())
]+ router.urls