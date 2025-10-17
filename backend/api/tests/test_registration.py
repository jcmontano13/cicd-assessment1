from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import User
from rest_framework import status

print(">>> test_registration.py loaded")

class UserRegistrationTest(APITestCase):
    def test_user_can_register(self):
        print(">>> test_user_can_register running")
        url = reverse('register')
        data = {
            "email": "test@example.com",
            "display_name": "testuser",
            "password": "securepass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(display_name="testuser").exists())
