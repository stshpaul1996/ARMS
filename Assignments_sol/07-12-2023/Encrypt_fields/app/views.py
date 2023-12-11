from .models import employee
from django.http import HttpResponse
def insert_data(request):
    emp =employee(name='Mallu Eswar',password='!@#$%^&*(',desi='software labour')
    emp.save()
    k=employee.objects.all()
    res=[i.password for i in k]
    print(res)
    return HttpResponse('<p>done</p>')

