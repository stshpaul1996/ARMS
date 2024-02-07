from .models import * 
from rest_framework import serializers 
from django.core.exceptions import ValidationError

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username','password','role']



class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = "__all__"

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

        
class permissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"