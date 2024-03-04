from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user',UserModelViewset,basename='user')
router.register(r'userprofile',UserProfileModelviewset,basename='userprofile')
router.register(r'parent',ParentModelviewset,basename ='parent')
router.register(r'child',ChildModelviewset,basename = 'child')

urlpatterns = [
    
]+router.urls