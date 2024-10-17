from django.contrib import admin
from .models import HazardousMaterial,TransportRecord
# Register your models here.
admin.site.register(HazardousMaterial)

admin.site.register(TransportRecord)