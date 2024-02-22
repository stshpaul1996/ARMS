from django.test import TestCase

from rest_framework.test import APIClient

class UserRegistrationTest(TestCase):
    client = APIClient()

    @classmethod 
    def setUpClass(cls):
        r1 = cls.client.post("/role/", data={"name":"admin"})
        cls.role_id = r1.data.get("id")

    def test_positive_user(self):
        #r1 = self.client.post("/role/", data={"name":"admin"})
        resp = self.client.post("/user/", data = {'username':"nithisha","password":"nithisha", 
                                                              "role":self.role_id})
        
        self.assertEqual(resp.status_code,201)


    @classmethod
    def tearDownClass(cls):
        print("done")