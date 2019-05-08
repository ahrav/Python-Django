from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from .models import Status

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class StatusAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='username', email='email@email.com')
        user.set_password('password')
        user.save()
        Status.objects.create(user=user, content='hello')

    def test_statuses(self):
        self.assertEqual(Status.objects.count(), 1)

    def status_user_token(self):
        auth_url = api_reverse('accounts:login')
        auth_data = {
            'username': 'username',
            'password': 'password',
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get('token', 0)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token()
        url = api_reverse('status:list')
        data = {
            'content': 'cool test stuff'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)
        return response.data

    # CREATE
    def test_status_create(self):
        data = self.create_item()
        data_id = data.get('id')
        url = api_reverse('status:detail', kwargs={'id': data_id})
        data = {
            'content': 'new coolercool test stuff'
        }
        get_response = self.client.get(url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    # UPDATE
    def test_status_updated(self):
        data = self.create_item()
        data_id = data.get('id')
        url = api_reverse('status:detail', kwargs={'id': data_id})
        data = {
            'content': 'new coolercool test stuff'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertEqual(response_data['content'], data['content'])

    # DELETE 
    def test_status_delete(self):
        data = self.create_item()
        data_id = data.get('id')
        url = api_reverse('status:detail', kwargs={'id': data_id})
        data = {
            'content': 'new coolercool test stuff'
        }
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # NOT FOUND
        get_response = self.client.get(url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token_create(self):
        url = api_reverse('status:list')
        data = {
            'content': 'cool test stuff'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
