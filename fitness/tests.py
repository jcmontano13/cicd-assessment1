from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone


class ActivityLoggingTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            password="securepassword",
            display_name="Test User"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.url = reverse("activity-create")

    def test_log_activity_success(self):
        payload = {
            "activity_type": "Running",
            "date_time": timezone.now().isoformat(),
            "duration": str(timedelta(minutes=45)),
            "status": "Completed",
            "remarks": "Morning jog around the park"
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["activity_type"], "Running")
        self.assertEqual(response.data["status"], "Completed")
        self.assertEqual(response.data["user"], self.user.id)

    def test_log_activity_missing_fields(self):
        payload = {
            "activity_type": "Cycling"
            # Missing date_time, duration, status, remarks
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


from django.test import TestCase

# Create your tests here.
