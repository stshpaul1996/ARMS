from django.test import TestCase
from rest_framework.test import APIClient
import unittest

# Create your tests here.
class SampleTest(TestCase):
    client = APIClient()
    @classmethod
    def setUpClass(cls):
        import pdb;pdb.set_trace()

        role_inst=cls.client.post("/role/",data={"name":"admin"})
        cls.role_inst=role_inst.json().get("id")

    def test_positive_user_reg(self):
        print("THis is test1")
       
        print(self.role)
        resp=self.client.post("/user/",data={"username":"bhag","password":"123","root":self.role_inst})
        self.assertEqual(resp.status_code,201)

    @classmethod
    def tearDown(cls):
        print("This is teardown class")

if __name__ == "__main__":
    unittest.main()


