from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.

class userregTest(TestCase):
    client = APIClient()
    def test_positive_reg(self):
        reg = self.client.post('/app1/user/', data={"username":"admin5", "password":"admin5"})
        # import pdb; pdb.set_trace()
        self.assertEqual(reg.status_code,201)

    # def test_positive_tk(self):
    #     reg = self.client.post('/app1/token/', data={"username":"admin5", "password":"admin5"})
    #     # import pdb; pdb.set_trace()
    #     self.assertEqual(reg.status_code,201)