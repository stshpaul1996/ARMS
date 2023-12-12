from django.urls import path
from .views import home_view
from .views import veg_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home_view),
    path("veg/",veg_view),
] +static("/static",document_root=settings.STATIC_ROOT)
