from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SampleView(APIView):
    def get(self,request):
        return Response('Get')
    
    def post(self,request):
        return Response('Post')
