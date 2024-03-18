from rest_framework import serializers
from . models import Role,MyUser,Customer,Premium,Claims,Expanses

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["username","password","role"]
        extra_kwargs={"password":{"write_only":True}}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ="__all__"

class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields ="__all__"

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields ="__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanses
        fields ="__all__"

        