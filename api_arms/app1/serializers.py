from rest_framework import serializers 
from app1.models import Person, Product, Category
from django.core.exceptions import ValidationError

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.Serializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
    name = serializers.CharField(max_length=250)
    category = serializers.IntegerField()
    product_unque_number = serializers.IntegerField()

    # def save():
    #     model_instance
    #     save()
    
class ProductModelSerializer(serializers.ModelSerializer):
    # cost = # that should directly reffer the models.ProductCost.cost#serializers.DecimalField(max_digits=10, decimal_places=2)
    # openingstock =#that should directly reffer the models.Openingstock.stock #serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock =serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields = ("name", "product_unque_number", "category",
                  "cost","openingstock")
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def validate_name(self, value=None):
        if value.isalnum():
            return value.upper()
            #return value
        raise ValidationError("exepcting alpha numneric value.")
    
    # def validate(self, data):
    #     #self.validated_data = super(PersonSerializer, self).validate(*args)
    #     import pdb;pdb.set_trace()
        
    #     data = self.initial_data
    #     age = data.get("age")
    #     if age and age>=18:
    #         if not data.get("email"):
    #             raise ValidationError("Email mandatory")
    #     return super(PersonSerializer, self).validate(*args)

           

    # def clean_name(self, value=None):
    #     import pdb;pdb.set_trace()
    #     print("hello")

    
