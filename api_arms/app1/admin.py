
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([ProductCost,OpeningStock,Product,PurchaseOrder,SalesOrder,Person,Category])

from django.contrib import admin
