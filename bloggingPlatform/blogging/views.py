from django.shortcuts import render
from .serializers import PostSerializer,CommentSerializer,PostCommentSerializer
from .models import PostModel,CommentModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# Create your views here.

class postView(APIView):
    def get(self,request,id = None):
        if id != None:
            ins = PostModel.objects.get(id = id)
            ser = PostSerializer(ins)
            return Response(ser.data)
        else:
            ins = PostModel.objects.all()
            ser = PostSerializer(ins,many=True)
            return Response(ser.data)

    def post(self,request):

        ser = PostSerializer(data=request.data)
        
        if ser.is_valid():
            ser.save()
            return Response("Data Submitted Succesfully")
        
        return Response(ser.errors) 

    def put(self,request,id):
        ins = PostModel.objects.get(id=id)
        ser = PostSerializer(ins,request.data)

        if ser.is_valid():
            ser.save()
            return Response("Data Updated Successfully")
        return Response(ser.errors)

    def delete(self,request,id):
        ins = PostModel.objects.get(id = id)
        ser = PostSerializer(ins)
        ser.delete()
        return Response("Data Deleted Successfully")

class commentView(APIView):
    # def get(self,request,id = None):
    #     if id != None:
    #         ins = CommentModel.objects.get(id = id)
    #         ser = CommentSerializer(ins)
    #         return Response(ser.data)
    #     else:
    #         ins = CommentModel.objects.all()
    #         ser = CommentSerializer(ins,many = True)
    #         data = ser.data
    #         for comment_data in data:
    #             comment_data['post'] = PostCommentSerializer(comment_data['post']).data
        
    #         return Response(data)
    #     return Response(ser.errors)

    def get(self, request, id=None):
        try:
            if id is not None:
                instance = CommentModel.objects.get(id=id)
                serializer = CommentSerializer(instance)
                return Response(serializer.data)
            else:
                instances = CommentModel.objects.all()
                serializer = CommentSerializer(instances, many=True)
                data = serializer.data
                for comment_data in data:
                    comment_data['post'] = PostCommentSerializer(comment_data['post']).data
                return Response(data)
        except CommentModel.DoesNotExist:
            return Response("Comment not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        ser = CommentSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response("Data submitted Successfully")
        return Response(ser.errors)

    def put(self,request,id):
        ins = CommentModel.objects.get(id=id)
        ser = CommentSerializer(ins,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("Data updated Successfully")
        return Response(ser.errors)

    def delete(self,request,id):
        ins = CommentModel.objects.get(id = id)
        ser = CommentSerializer(ins)
        ser.delete()
        return Response("Data Deleted Successfully")






