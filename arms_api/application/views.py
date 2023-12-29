from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class SampleView(APIView):
    def post(self,request):
        return Response("post") #the consumer of the api is expecting json response
    
    def get(self,request,**kwargs):
        return Response("get")
    
    def delete(self,request,**kwargs):
        return Response("delete")
    
    def put(self,request,**kwargs):
        return Response("put")
      
    def patch(self,request,**kwargs):
        return Response("patch")
    