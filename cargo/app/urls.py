from django.urls import path
from .views import upload_and_process_image, display_placard, generate_invoice

urlpatterns = [
    path('upload/', upload_and_process_image, name='upload_image'),
    path('placard/<str:un_number>/', display_placard, name='display_placard'),
    path('invoice/<int:transport_record_id>/', generate_invoice, name='generate_invoice'),
]
