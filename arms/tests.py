from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
class userRegistration(TestCase):
    client = APIClient()
    def test_positive_user_reg(self):
        # import pdb;pdb.set_trace()
        # resp = self.client.post('/role/',data = {"name":"user3"})
        # role_id = resp.json().get("name")
        resp = self.client.post("/trip/",data = {"name":"locknow"})
        # import pdb;pdb.set_trace()
        self.assertEqual(resp.status_code,201)