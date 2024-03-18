from inheritance_app. models import Employee

# Create your models here.
class Proxy_model(Employee):
    class Meta:
        proxy=True
        ordering=["-emp_salary"]
