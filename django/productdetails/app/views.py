from django.shortcuts import render
from .models import Product
# Create your views here.

def product_view(request):
    data=Product.objects.all()
    return render(request,'product.html',{'data':data,'header':'List of product'})