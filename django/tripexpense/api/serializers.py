from rest_framework import serializers
from .models import Member, Expense, Trip

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    # members = MemberSerializer(many=True,read_only=True)
    # expenses = ExpenseSerializer(many=True,read_only=True)
    
    class Meta:
        model = Trip
        fields = '__all__'
    