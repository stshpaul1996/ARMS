from django.urls import path
from app.views import Travel

urlpatterns = [
    path("<str:name>/",Travel)
]
