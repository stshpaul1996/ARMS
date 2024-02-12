from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

class UserRegisterTest(TestCase):
    client  = APIClient
    def test_positive_user_regi(self):
        res = self.client.post('/login',headers ={},data="username":"ruchi",'password':"ruchi")
        self.assertEqual(res,status_code)

