from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SampleAPIView(APIView):
    def get(self,request,*args,**kwargs):
        return Response("get")
    
    def post(self,request,*args,**kwargs):
        print(request.data)
        print(type(request.data))
        return Response("post")
    
    def put(self,request,*args,**kwargs):
        return Response("put")

    def patch(self,request,*args,**kwargs):
        return Response("patch")
    
    def delete(self,request,*args,**kwargs):
        return Response("delete")
    