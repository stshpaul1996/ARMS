from django.contrib import admin
from .models import Category, PurchaseOrder, SalesOrder, Product, ProductCost, OpeningStock, ProductPurchases, ProductSales, Stock

# Register your models here.
admin.site.register([Category, PurchaseOrder, SalesOrder, Product, ProductCost, OpeningStock, ProductPurchases, ProductSales, Stock
])