from django.urls import path
from app1.views import LoginApi,UserCreation
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserCreation, basename="user")

urlpatterns = [
    path("user_login/",LoginApi.as_view())
    # path("user_create/",UserCreation.as_view())
]+ router.urls
