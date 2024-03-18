from rest_framework import routers
from . import views
from django.urls import path
router=routers.DefaultRouter()
router.register('api',views.ApiViewSet)
router.register('role',views.RoleViewSet)
router.register('myuser',views.MyUserViewSet)
router.register('permission',views.PermissionViewSet)
router.register('dept',views.DepartmentsViewSet)
router.register('emp',views.EmployeeViewSet)
urlpatterns = [
    path('login/',views.LoginAPIView.as_view()),
]+router.urls