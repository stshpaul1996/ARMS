from django.shortcuts import render
from .models import Product
# Create your views here.

def product_view(request):
    data=Product.objects.all()
    return render(request,'product.html',{'data':data,'header':'List of product'})

def addproduct_view(request):
    message=''
    if request.method=='POST':
        data=request.POST
        obj=Product(name=data['product_name'],price=data['product_price'],img=data['product_img'])
        obj.save()
        message='product added successful'
    else:
        message=''
    return render(request,'addproduct.html',{'message':message})