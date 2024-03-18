from . views import UserProfileViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('api',UserProfileViewSet)
urlpatterns=[
]+router.urls

