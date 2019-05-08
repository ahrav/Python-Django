from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='username', email='email@email.com')
        user.set_password('password')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='username')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_success(self):
        url = api_reverse('accounts:register')
        data = {
            'username': 'user',
            'email': 'user@user.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get('token', 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api_success(self):
        url = api_reverse('accounts:login')
        data = {
            'username': 'username',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        url = api_reverse('accounts:login')
        data = {
            'username': 'usernamedd',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_token_login_api(self):
        url = api_reverse('accounts:login')
        data = {
            'username': 'username',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        url = api_reverse('accounts:login')
        data = {
            'username': 'username',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        url2 = api_reverse('accounts:register')
        data2 = {
            'username': 'user',
            'email': 'user@user.com',
            'password': 'password',
            'password2': 'password'
        }
        response2 = self.client.post(url2, data2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)