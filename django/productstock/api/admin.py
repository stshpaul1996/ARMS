from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=['name']

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
    list_display=['product_id','description','purchasestock']

@admin.register(SSOS)
class AdminSSOS(admin.ModelAdmin):
    list_display=['product_id','description','salestock']

@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    list_display=['description','product_id','type','stock']

