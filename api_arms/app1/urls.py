<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from app1.views import (SampleView, ProductView, CategoryView,PoductCostOpeningstockView)

urlpatterns = [
    # path("person/<int:pk>/", SampleView.as_view()),
    path("person/", SampleView.as_view()),
    path("product/", ProductView.as_view()),
    path("category/", CategoryView.as_view()),
    path("diff_data", PoductCostOpeningstockView.as_view()),

    
    
]
=======
from django.contrib import admin
from django.urls import path, include
from app1.views import (SampleView, ProductView, CategoryView)
from app1.viewsets import PersonModelViewset, UserViewSet, RoleModelViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'viewset_person', PersonModelViewset, basename='viewset_person')
router.register(r'user', UserViewSet, basename="user")
router.register(r'role', RoleModelViewset, basename='role')
router.register(r'api', PersonModelViewset, basename='api')
router.register(r'permission', PersonModelViewset, basename='permission')
router.register(r'viewset_person', PersonModelViewset, basename='viewset_person')


urlpatterns = [
    # path("person/<int:pk>/", SampleView.as_view()),
    path("person/", SampleView.as_view()),
    path("product/", ProductView.as_view()),
    path("category/", CategoryView.as_view()),

    # path("viewset_person/", PersonViewset.as_view({"post": "post_method"}))
    # path("viewset_person/<int:pk>", PersonViewset.as_view({"put": "put_method",
    #                                                        "delete": "delete_method"}))
    
    
] + router.urls
>>>>>>> 7aaa55c3dc0d9b8880651676d930355cef0e1f4c
