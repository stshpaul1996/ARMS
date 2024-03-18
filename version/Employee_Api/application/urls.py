from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user',views.UserViewSet)
urlpatterns = [
    path('api/',views.LoginAPIView.as_view())
]+router.urls