from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Role, Person, API, Permissions,MyUser
class RoleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_role(self):
        response = self.client.post('/role/', data={'name': 'Admin'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Role.objects.filter(name='Admin').exists())
        self.role_id = response.data.get("id")
    def test_retrieve_role(self):
        role = Role.objects.create(name='Admin')
        response = self.client.get(f'/role/{role.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Admin')

    def test_update_role(self):
        role = Role.objects.create(name='Admin')
        response = self.client.put(f'/role/{role.id}/', {'name': 'Updated Role'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Role.objects.get(id=role.id).name, 'Updated Role')

    def test_delete_role(self):
        role = Role.objects.create(name='Admin')
        response = self.client.delete(f'/role/{role.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Role.objects.filter(id=role.id).exists())


class UserRegisterTest(TestCase):
    client  = APIClient()
    
    @classmethod
    def setUpClass(cls) -> None:
        role  = cls.client.post("/role/",data={"name":"admin"})
        cls.role_id  =role.data.get("id")
        cls.role = Role.objects.create(name='admin')
    def test_create_user(self):
        res = self.client.post("/user/",headers ={},data={"username":"ruchi",'password':"ruchi","email":"dskj@gmail.com","role":self.role_id})
        self.assertEqual(res.status_code,201)
    #import pdb;pdb.set_trace()
    def test_retrieve_user(self):
        user = MyUser.objects.create(username='admin',role = self.role)
       
        response = self.client.get(f'/user/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'admin')

    def test_update_user(self):
        user = MyUser.objects.create(username='admin', role=self.role)
        new_username = 'updated_admin'
        
        # Update the user's username
        response = self.client.put(f'/user/{user.id}/', {'username': new_username, 'password':"abc",'role': self.role.id}, content_type='application/json')
       #print(response.content)
        # Assert that the status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Retrieve the updated user from the database and verify the username
        updated_user = MyUser.objects.get(id=user.id)
        self.assertEqual(updated_user.username, new_username)


    def test_delete_user(self):
        user = MyUser.objects.create(username='admin', role=self.role)
        
        # Delete the user
        response = self.client.delete(f'/user/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify that the user is deleted from the database
        self.assertFalse(MyUser.objects.filter(id=user.id).exists())
    @classmethod
    def tearDownClass(cls) -> None:
        print("done")

# class LoginAPITest(UserRegisterTest):
#     def setUp(self):
        
#         self.client = APIClient()
#         self.role = self.client.post("/role/",data = {"name":"admin"})
#         self.user = get_user_model().objects.create_user(username='testuser', password='password',role =self.role_id)
#     def test_login_success(self):
#         #import pdb;pdb.set_trace()
#         # Create a valid login request data
#         data = {"username": "admin", "password": "password","role":self.role_id}

#         # Send POST request to the LoginAPI
#         response = self.client.post('/login/', data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('token', response.data)

#     def test_login_failure(self):
#         # Create invalid login request data (wrong password)
#         data = {"username": "testuser", "password": "wrongpassword"}

#         # Send POST request to the LoginAPI
#         response = self.client.post('/login/', data, format='json')

#         # Check if the response status code is 401 (Unauthorized)
#         self.assertEqual(response.status_code, 401)

#         # Check if the response does not contain a token
#         self.assertNotIn('token', response.data)
