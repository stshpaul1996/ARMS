from django.shortcuts import render
from .models import Product
# Create your views here.
def Product_detail(request):
    obj = Product.objects.all()


    return render(request,'app1/product_details.html',{'obj':obj})