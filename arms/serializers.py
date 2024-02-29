from rest_framework import serializers

from arms.models import MyUser,Role,trip,member,expenses,Permission,Api,Role

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username","password","email","role"]

class Roleserializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id',"name"]

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = "__all__"

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = expenses
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"