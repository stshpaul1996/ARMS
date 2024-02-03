from django.urls import path
from app2.views import JonerViewSet,MovieViewSet,get_jone_ratings

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('jones', JonerViewSet, basename="jones")
router.register('movies', MovieViewSet, basename='movies')


urlpatterns = [
        path('jones/<int:jone_id>/<str:start_date>/<str:end_date>/', get_jone_ratings, name='jone_ratings'),
]+router.urls