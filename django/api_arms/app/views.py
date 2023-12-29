from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee,Department
# Create your views here.

class SampleView(APIView):
    def post(self,request):
        msg=''
        try:
            emp=Employee(name=request.data.get('name'),job_name=request.data.get('job_name'),
                     salary=request.data.get('salary'),hire_date=request.data.get('hire_date'))
            dept_id = request.data.get('dept_id')
            department_instance = Department.objects.get(pk=dept_id)

            emp.dept_id = department_instance
        
            emp.save()
            msg=('inserted successfully')
        except Exception as err:
            msg=str(err)
        return Response({'msg':msg})
    
    def get(self,request):
        emp=Employee.objects.all()
        data=[{'name':i.name,'job_name':i.job_name,'salary':i.salary,'hire_date':i.hire_date,'dept_id':i.dept_id.id} for i in emp]
        return Response(data)
    
   
    def put(self, request, pk):
        msg = ''
        try:
            
            emp = Employee.objects.get(pk=pk)
            emp.name = request.data.get('name', emp.name)
            emp.job_name = request.data.get('job_name', emp.job_name)
            emp.salary = request.data.get('salary', emp.salary)
            emp.hire_date = request.data.get('hire_date', emp.hire_date)

            
            dept_id = request.data.get('dept_id')
            if dept_id:
                department_instance = Department.objects.get(pk=dept_id)
                emp.dept_id = department_instance

            emp.save()
            msg = 'Updated successfully'
        except Employee.DoesNotExist:
            msg = 'Employee not found'
        except Department.DoesNotExist:
            msg = 'Department not found'
        except Exception as err:
            msg = str(err)

        return Response({'msg': msg})


    def patch(self,request):
        return Response('patch')
    def delete(self,request,pk):
        msg=''
        print(dir(Exception))
        try:
            emp=Employee.objects.get(pk=pk)
            emp.delete()
            msg='deleted successfull'
            
        except Employee.DoesNotExist:
            msg='Employee not Found'
        except Exception as err:
            msg=str(err)
        return Response({'msg':msg})