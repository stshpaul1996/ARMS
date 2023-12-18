from django.urls import path
from .views import personalities
urlpatterns = [
    path('<str:name>',personalities,name='cricketers')
]