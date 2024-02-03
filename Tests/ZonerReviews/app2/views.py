from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from app2.models import Joner,Movie
from app2.serializers import JonerSerializer,MovieSerializer
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from datetime import datetime
from django.utils import timezone




class JonerViewSet(viewsets.ModelViewSet):
    queryset = Joner.objects.all()
    serializer_class = JonerSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def create(self,request,*args, **kwargs):
    #     # super().create(self*args, **kwargs)
    #     print(request.user)
    #     print(request)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     serializer.validated_data['created_by'] = request.user
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     if not instance.status:
    #         serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.validated_data["updated_date"] = timezone.now()
    #         serializer.validated_data["updated_by"] = request.user
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    #     else:
    #         msg = "No data found"
    #         return Response(msg,status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_jone_ratings(request, jone_id, start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    jone = get_object_or_404(Joner, pk=jone_id)
    movies_within_range = Movie.objects.filter(joner=jone, release_date__range=(start_date, end_date))
    avg_rating = movies_within_range.aggregate(Avg('rating'))['rating__avg']
    response_data = {
        "jone_name": jone.name,
        "start_date": start_date,
        "end_date": end_date,
        "average_rating": avg_rating,
    }

    return JsonResponse(response_data)


