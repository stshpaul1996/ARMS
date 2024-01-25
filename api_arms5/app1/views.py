from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class login_view(APIView):
    def post(self, request):
        return Response('You have logged in.')