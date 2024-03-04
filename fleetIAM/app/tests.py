from django.test import TestCase


from rest_framework.test import APIClient

class UserRegisterTest(TestCase):
    client  = APIClient()
    
    @classmethod
    def setUpClass(cls) -> None:
        role  = cls.client.post("/role/",data={"name":"admin"})
        cls.role_id  =role.data.get("id")
    def test_positive_user_regi(self):
        #import pdb;pdb.set_trace()
       # role = self.client.post("/role/",headers ={},data={"name":"admin"})
        res = self.client.post("/user/",headers ={},data={"username":"ruchi",'password':"ruchi","email":"dskj@gmail.com","role":self.role_id})
        self.assertEqual(res.status_code,201)
    @classmethod
    def tearDownClass(cls) -> None:
        print("done")
