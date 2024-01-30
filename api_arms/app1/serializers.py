from rest_framework import serializers 
from app1.models import Person, Product, Category,OpeningStock,ProductCost
from django.core.exceptions import ValidationError
from app1.models import Role, MyUser
class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    #role = serializers.IntegerField()

    class Meta:
        model = MyUser
        fields = ["username", "password","email", "role"]

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PoductCostOpeningstockSerializer(serializers.Serializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
    name = serializers.CharField(max_length=250)
    category = serializers.IntegerField()
    product_unque_number = serializers.CharField()
    purchase_orders=serializers.CharField(max_length=250)
    sales_orders=serializers.CharField(max_length=250)


    # def save():
    #     model_instance
    #     save()
    def create(self, validated_data):
        cost = validated_data.pop('cost')
        openingstock = validated_data.pop('openingstock')
        product = Product.objects.create(**validated_data)
        ProductCost.objects.create(product=product, cost=cost)
        OpeningStock.objects.create(product=product, stock=openingstock)
        return product


class ProductModelSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    # cost = # that should directly reffer the models.ProductCost.cost#serializers.DecimalField(max_digits=10, decimal_places=2)
    # openingstock =#that should directly reffer the models.Openingstock.stock #serializers.DecimalField(max_digits=10, decimal_places=2)
=======
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
>>>>>>> 7aaa55c3dc0d9b8880651676d930355cef0e1f4c
    class Meta:
        model = Product
        fields = ("name", "product_unque_number", "category",
                  "cost","openingstock")

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        #fields = "__all__"
        exclude = ('created_by', )

    def validate_name(self, value=None):
        if value.isalnum():
            return value.upper()
            #return value
        raise ValidationError("exepcting alpha numneric value.")
    
    def validate(self, data):
        #self.validated_data = super(PersonSerializer, self).validate(*args)
        
        data = self.initial_data
        age = data.get("age")
        if age and age>=18:
            if not data.get("email"):
                raise ValidationError("Email mandatory")
<<<<<<< HEAD
        return super(PersonSerializer, self).validate()
=======
        return super(PersonSerializer, self).validate(data)
>>>>>>> 7aaa55c3dc0d9b8880651676d930355cef0e1f4c

        

    
