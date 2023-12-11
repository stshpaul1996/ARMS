from .models import employee
from django.http import HttpResponse
def insert_data(request):
    emp =employee(name='boby',password='123456789',desi='software engineer')
    emp.save()
    k=employee.objects.all()
    res=[i.password for i in k]
    print(res)
    return HttpResponse('<p>done</p>')

