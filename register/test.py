from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.payload = {
            "email": "ciuser@example.com",
            "password": "testpass123",
            "display_name": "CI User"
        }
        self.url = reverse("register")

    def test_registration_and_duplicate(self):
        response1 = self.client.post(self.url, self.payload, content_type="application/json")
        self.assertIn(response1.status_code, [200, 201])

        response2 = self.client.post(self.url, self.payload, content_type="application/json")
        self.assertEqual(response2.status_code, 400)

    def tearDown(self):
        CustomUser.objects.filter(email=self.payload["email"]).delete()