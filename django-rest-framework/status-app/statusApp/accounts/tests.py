from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='username', email='email@email.com')
        user.set_password('password')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='username')
        self.assertEqual(qs.count(), 1)