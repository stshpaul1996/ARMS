from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
import unittest

class SampleTest(TestCase):
    client=APIClient()
    @classmethod
    def setUpClass(cls):
        #write login code
        #import pdb;pdb.set_trace()
        r=cls.client.post("/role/",data={"id":7,"name":"user45"})
        #import pdb;pdb.set_trace()
        cls.role_id=r.data.get('id')

    def test_posivite_user_reg(self):
        resp=self.client.post("/user/",data={"username":"user6","password":"root","role":self.role_id})
        #import pdb;pdb.set_trace()
        self.assertEqual(resp.status_code,201)
      
    @classmethod
    def tearDownClass(cls):
        print('this is teardown class')


class UserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()
        resp = cls.client.post("/role/", data={"name": "admin1"})
        cls.role_id = resp.json().get("id")
        
    @classmethod
    def tearDownClass(cls):
        resp = cls.client.delete(f"/role/{cls.role_id}/")
        #cls.assertEqual(resp.status_code, 200)
          
    def test_user_creation(self):
        resp = self.client.post("/user/", data={"username": "admin", "password": "password", "role": self.role_id,"email": "admin@example.com"})
        self.assertEqual(resp.status_code, 201)
        resp = self.client.delete(f"/user/{resp.json().get('id')}")
        self.assertEqual(resp.status_code, 301)