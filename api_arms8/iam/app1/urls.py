from django.urls import path
from .views import*


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'user', UserViewSet, basename="user")

urlpatterns = [
   path('token/', Login_api.as_view()),
   
]+ router.urls