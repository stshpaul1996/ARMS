from django.test import TestCase
from rest_framework.test import APIClient
 
class UserRegisterTest(TestCase):
    client  = APIClient()
    def test_positive_reg(self):
        reg = self.client.post('/app1/token/', data= {"username":"admin", "password":"admin"})
        self.assertEqual(reg.status_code,201)