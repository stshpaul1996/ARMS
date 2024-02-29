from rest_framework import serializers
from .models import ProxyUserProfile, Visits

class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyUserProfile
        fields = ["username", "pancard"]

        def username(self,value):
            return value.username_with_username

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = "__all__"
    

    