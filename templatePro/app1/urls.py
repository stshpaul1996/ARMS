from django.urls import path,include
from .views import home_view, tech_view, science_view, health_view,business_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", home_view),
    path("tech/",tech_view ),
    path("science/", science_view),
    path("health/", health_view),
    path("business/", business_view)
]+static('/static',dcoument_root=settings.STATIC_ROOT)
