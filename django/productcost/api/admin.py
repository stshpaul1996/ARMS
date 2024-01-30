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
    list_display=['name','product_unique_number','category']

@admin.register(OpeningStock)
class AdminOpeningStock(admin.ModelAdmin):
    list_display=['prodcut','stock']

@admin.register(CostPrice)
class AdminCostPrice(admin.ModelAdmin):
    list_display=['product_id','cost']

@admin.register(PPOS)
class AdminPPOS(admin.ModelAdmin):
    list_display=['product_id','purchase_id','stock']

@admin.register(SSOS)
class AdminSSOS(admin.ModelAdmin):
    list_display=['product_id','sale_id','stock']

@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    list_display=['description','product','type','stock']

@admin.register(FinalStockReport)
class AdminFinalStockReport(admin.ModelAdmin):
    list_display=['name','product_unique_number','category']
    