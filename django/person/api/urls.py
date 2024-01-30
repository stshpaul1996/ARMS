
from django.urls import path
from api.views import PersonVeiw,CustomAuthToken
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('person', PersonVeiw, basename='person')
urlpatterns = [
    path('token/',CustomAuthToken.as_view())
    
]+router.urls