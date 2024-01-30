from app1.views import UserViewSet, RoleModelViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleModelViewset, basename='role')
# router.register(r'api', PersonModelViewset, basename='api')
# router.register(r'permission', PersonModelViewset, basename='permission')
# router.register(r'viewset_person', PersonModelViewset, basename='viewset_person')


urlpatterns = [
    
] + router.urls