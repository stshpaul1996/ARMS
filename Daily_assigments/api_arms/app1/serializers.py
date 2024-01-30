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
        fields = "__all__"
        # exclude = ('created_by', 'updated_by')

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

        

    
# class UserSerializers(serializers.ModelSerializer):
# # groups = GroupSerializer(many=True)

# class Meta:
#     model = User
#     fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'address', 'is_active', 'is_staff',
#           'is_superuser', 'date_joined', 'password', 'groups')

# def create(self, validated_data):
#     groups_data = validated_data.pop('groups')
#     user = User.objects.create(**validated_data)
#     for group_data in groups_data:
#         # Group.objects.create(user=user, **group_data)
#         user.groups.add(group_data)
#     return user