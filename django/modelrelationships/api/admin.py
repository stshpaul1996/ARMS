from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=['name']

@admin.register(SalesOrder)
class AdminSalesOrder(admin.ModelAdmin):
    list_display=['description']

@admin.register(PurchaseOrder)
class AdminPurchaseOrder(admin.ModelAdmin):
    list_display=['description']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['name','product_unque_number','category']

@admin.register(OpeningStock)
class AdminOpeningStock(admin.ModelAdmin):
    list_display=['prodcut','stock']

