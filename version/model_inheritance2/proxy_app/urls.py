from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('proxy',views.Proxy_viewset,basename='proxy')
urlpatterns = [
]+router.urls