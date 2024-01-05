from django.urls import path
from .views import home_view, kohli_view, cricketer_view, cricketer_view_id, cricketers_view,\
cricketer_add_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home_view),
    path("cricketers/", cricketers_view),
    path("addcricketer/", cricketer_add_view),
    path("<str:cricketer>/", cricketer_view), #/app1/rohit: cricketer_view(request_obj, cricketer='rohit')
    path("<int:cricketer_id>/", cricketer_view_id), #/app1/rohit: cricketer_view(request_obj, cricketer='rohit')
    path("kohli/", kohli_view),
] 
