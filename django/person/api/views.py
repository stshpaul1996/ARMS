from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import datetime
from rest_framework import status
# Create your views here.


class PersonVeiw(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_creation = instance.pk is None
        user_updating = self.request.user
        updated_date_str = datetime.now().isoformat() + "Z"
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=user_updating if is_creation else instance.created_by,
            updated_by=user_updating,
            updated_date=updated_date_str)
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        #import pdb;pdb.set_trace()
        #serializer = self.get_serializer(data=request.data)
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response({"data":"Status changed"},status=status.HTTP_200_OK)
    







class CustomAuthToken(ObtainAuthToken):
 def post(self, request, *args, **kwargs):
  serializer = self.serializer_class(data=request.data, context={'request': request})
  serializer.is_valid(raise_exception=True)
  user = serializer.validated_data['user']
  #import pdb;pdb.set_trace()
  token, created = Token.objects.get_or_create(user=user)
  return Response({
    'token': token.key,
     'user_id': user.pk,
     'email': user.email
  })