from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import CustomUser

class LoginTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="user@example.com",
            password="correctpassword",
            display_name="Jeck"
        )
        self.login_url = reverse("login")  # or use '/api/login/' directly

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            "email": "user@example.com",
            "password": "correctpassword"
        }, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("user_id", response.data)

    def test_login_failure_wrong_password(self):
        response = self.client.post(self.login_url, {
            "email": "user@example.com",
            "password": "wrongpassword"
        }, format="json")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["error"], "Invalid credentials")

    def test_login_failure_missing_fields(self):
        response = self.client.post(self.login_url, {
            "email": ""
        }, format="json")
        self.assertEqual(response.status_code, 400)