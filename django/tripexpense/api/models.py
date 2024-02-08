from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, related_name="%(class)s_created_by",on_delete=models.CASCADE,null=True)
    updated_by = models.ForeignKey(User,related_name="%(class)s_updated_by",on_delete=models.CASCADE,null=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    updated_date=models.DateTimeField(null=True)

    class Meta:
        abstract = True

class Member(BaseModel):
    name = models.CharField(max_length=255)

class Expense(BaseModel):
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

class Trip(BaseModel):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Member)
    expenses = models.ManyToManyField(Expense)

    def calculate_member_shares(self):
        total_expenses = sum(expense.amount for expense in self.expenses.all())
        member_shares = {}
        
        for member in self.members.all():
            member_expenses = self.expenses.filter(member=member)
            member_share = 0  # Initialize member_share
            if total_expenses != 0:
                member_share = sum(expense.amount for expense in member_expenses) / total_expenses
            member_shares[member.name] = member_share
            print(member_share)

        return member_shares
