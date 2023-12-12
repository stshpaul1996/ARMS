
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.home_view,),
    path('prime/',views.Prime),
    path('bumblebee/',views.Bumblebee),
    path('megatron/',views.Megatron),
    path('grimlock/',views.Grimlock),

] +static('/static', document_root =settings.STATIC_ROOT)
