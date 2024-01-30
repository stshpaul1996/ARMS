from rest_framework import serializers 
from app1.models import Person, Product, Category
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

class ProductSerializer(serializers.Serializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
    name = serializers.CharField(max_length=250)
    category = serializers.IntegerField()
    product_unque_number = serializers.IntegerField()

    def save():
        model_instance
        save()
    
class ProductModelSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    openingstock = serializers.DecimalField(max_digits=10, decimal_places=2)
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
        return super(PersonSerializer, self).validate(data)

        

    
