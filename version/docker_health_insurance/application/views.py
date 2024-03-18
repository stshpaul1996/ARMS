from . models import Customer,Premium,Claims,Expanses
from . serializers import CustomerSerializer,PremiumSerializer,ClaimSerializer,ExpenseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum
from django.contrib.auth.models import User
import logging
logger=logging.getLogger(__name__)

# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        logger.info("user creation started")
        logger.debug("")
        logger.error("")
        logger.warning("")
        data = super().create(request, *args, **kwargs).data
        logger.debug(f"user {data.get("username")} creating")
        user_id = request.user.id if request.user.is_authenticated else None
        customer_instance = Customer.objects.get(pk=data.get('id'))
        if user_id is not None:
            user_instance = User.objects.get(pk=user_id)
            customer_instance.created_by = user_instance
            logger.info("user created")
        else:
            customer_instance.created_by = None
        customer_instance.save()
        result = {"msg": "data added successfully", "id": customer_instance.id}
        return Response(result)
    
    def update(self, request, pk=None, *args, **kwargs):
        data = super().update(request, pk=pk, *args, **kwargs).data
        result = {"msg": "data not updated", "id": ""}
        user = request.user
        print("user details=",user)
        customer_instance = Customer.objects.get(pk=pk)
        if user.is_authenticated:
            customer_instance.updated_by = user
        else:
            customer_instance.updated_by = None
        customer_instance.save()
        result = {"msg": "data updated successfully", "id": customer_instance.id}
        return Response(result)
    

class PremiumView(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class=PremiumSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        user_id = request.user.id if request.user.is_authenticated else None
        premium_instance = Premium.objects.get(pk=data.get('id'))
        if user_id is not None:
            user_instance = User.objects.get(pk=user_id)
            premium_instance.created_by = user_instance
        else:
            premium_instance.created_by = None
        premium_instance.save()
        result = {"msg": "data added successfully", "id": premium_instance.id}
        return Response(result)
    
    def update(self, request, pk=None, *args, **kwargs):
        data = super().update(request, pk=pk, *args, **kwargs).data
        result = {"msg": "data not updated", "id": ""}
        user = request.user
        print("user details=",user)
        premium_instance = Premium.objects.get(pk=pk)
        if user.is_authenticated:
            premium_instance.updated_by = user
        else:
            premium_instance.updated_by = None
        premium_instance.save()
        result = {"msg": "data updated successfully", "id": premium_instance.id}
        return Response(result)

class ClaimsView(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class=ClaimSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        user_id = request.user.id if request.user.is_authenticated else None
        claim_instance = Claims.objects.get(pk=data.get('id'))
        if user_id is not None:
            user_instance = User.objects.get(pk=user_id)
            claim_instance.created_by = user_instance
        else:
            claim_instance.created_by = None
        claim_instance.save()
        result = {"msg": "data added successfully", "id": claim_instance.id}
        return Response(result)
    
    def update(self, request, pk=None, *args, **kwargs):
        data = super().update(request, pk=pk, *args, **kwargs).data
        result = {"msg": "data not updated", "id": ""}
        user = request.user
        print("user details=",user)
        claim_instance = Claims.objects.get(pk=pk)
        if user.is_authenticated:
            claim_instance.updated_by = user
        else:
            claim_instance.updated_by = None
        claim_instance.save()
        result = {"msg": "data updated successfully", "id": claim_instance.id}
        return Response(result)

class ExpenseView(viewsets.ModelViewSet):
    queryset=Expanses.objects.all()
    serializer_class=ExpenseSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        user_id = request.user.id if request.user.is_authenticated else None
        expanses_instance = Expanses.objects.get(pk=data.get('id'))
        if user_id is not None:
            user_instance = User.objects.get(pk=user_id)
            expanses_instance.created_by = user_instance
        else:
            expanses_instance.created_by = None
        expanses_instance.save()
        result = {"msg": "data added successfully", "id": expanses_instance.id}
        return Response(result)
    
    def update(self, request, pk=None, *args, **kwargs):
        data = super().update(request, pk=pk, *args, **kwargs).data
        result = {"msg": "data not updated", "id": ""}
        user = request.user
        print("user details=",user)
        expanses_instance = Expanses.objects.get(pk=pk)
        if user.is_authenticated:
            expanses_instance.updated_by = user
        else:
            expanses_instance.updated_by = None
        expanses_instance.save()
        result = {"msg": "data updated successfully", "id": expanses_instance.id}
        return Response(result)
    
class Profit_loss(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        total_premium=Premium.objects.all().aggregate(Sum('premium_amount'))['premium_amount__sum'] or 0
        total_claims=Claims.objects.all().aggregate(Sum('claim_amount'))['claim_amount__sum'] or 0
        total_expenses=Expanses.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
        profit_loss=total_premium-total_claims-total_expenses
        data={
            "total_premium":total_premium,
            "total_claims":total_claims,
            "total_expenses":total_expenses,
            "profit_loss":profit_loss
        }
        return Response(data)
    
    