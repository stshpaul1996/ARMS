from django.shortcuts import render
from datetime import datetime
import os
# Create your views here.
def welcome(request):
   print(os.environ)
   date = datetime.now()
   cont = {"key":date}
   return render(request,'testapp/welcome.html',context=cont)