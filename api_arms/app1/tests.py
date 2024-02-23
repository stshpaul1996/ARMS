from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient 

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
        resp = self.client.post("/user/", data={"username": "admin", "password": "password", 
                                                "role": self.role_id,"email": "admin@example.com"})
        self.assertEqual(resp.status_code, 201)
        resp = self.client.delete(f"/user/{resp.json().get('id')}")
        self.assertEqual(resp.status_code, 301)
        
        

