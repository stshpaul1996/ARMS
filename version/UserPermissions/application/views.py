from . models import Api,Role,Permission,MyUser,Department,Employee
from . serializers import APISerializer,PermissionsSerializer,RoleSerializer,MyUserSerializer,DepartmentSerializer,EmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
import jwt

# Create your views here.
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data=request.data
        res={"token":None,"msg":""}
        user=authenticate(**data)
        if user:
            # payload={"user":user.username}
            res["token"]=jwt.encode(data,"Bh@g@v@@n", algorithm="HS256")
            res["msg"]="ok"
            return Response(res,status=status.HTTP_201_CREATED)
        res["msg"]="Invalid details"
        return Response(res,status=status.HTTP_401_UNAUTHORIZED)
    

class ApiViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Api.objects.all()
    serializer_class = APISerializer

class RoleViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class MyUserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    
    def perform_create(self,serializer):
        data=serializer.data
        role_id=data.pop('role')
        role_inst=Role.objects.get(id=role_id)
        data['role']=role_inst
        MyUser.objects.create_user(**data)

class PermissionViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Permission.objects.all()
    serializer_class = PermissionsSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class=DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer

    

