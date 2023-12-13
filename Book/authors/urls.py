from django.urls import path,include
from .views import Details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:name>/',Details)
]+static('/static',document_root=settings.STATIC_ROOT)






