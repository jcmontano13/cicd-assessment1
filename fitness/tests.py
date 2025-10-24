from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone
from fitness.models import Activity

class ActivityLoggingTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            password="securepassword",
            display_name="Test User"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.create_url = reverse("activity-create")
        self.list_url = reverse("activity-list")

    def test_log_activity_success(self):
        payload = {
            "activity_type": "Running",
            "date_time": timezone.now().isoformat(),
            "duration": str(timedelta(minutes=45)),
            "status": "Completed",
            "remarks": "Morning jog around the park"
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["activity_type"], "Running")
        self.assertEqual(response.data["status"], "Completed")
        self.assertEqual(response.data["user"], self.user.id)

    def test_log_activity_missing_fields(self):
        payload = {
            "activity_type": "Cycling"
            # Missing date_time, duration, status, remarks
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_user_activities(self):
        Activity.objects.create(
            user=self.user,
            activity_type="Running",
            date_time=timezone.now(),
            duration=timedelta(minutes=30),
            status="Completed",
            remarks="Morning run"
        )
        Activity.objects.create(
            user=self.user,
            activity_type="Cycling",
            date_time=timezone.now(),
            duration=timedelta(minutes=45),
            status="Planned",
            remarks="Evening ride"
        )

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["user"], self.user.id)
        self.assertEqual(response.data[1]["user"], self.user.id)

    def test_view_individual_activity(self):
        activity = Activity.objects.create(
            user=self.user,
            activity_type="Swimming",
            date_time=timezone.now(),
            duration=timedelta(minutes=60),
            status="Completed",
            remarks="Evening swim at the pool"
        )
        detail_url = reverse("activity-detail", kwargs={"pk": activity.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], activity.pk)
        self.assertEqual(response.data["activity_type"], "Swimming")
        self.assertEqual(response.data["status"], "Completed")
        self.assertEqual(response.data["remarks"], "Evening swim at the pool")
        self.assertEqual(response.data["user"], self.user.id)

    def test_update_status_variants(self):
        activity = Activity.objects.create(
            user=self.user,
            activity_type="Yoga",
            date_time=timezone.now(),
            duration=timedelta(minutes=60),
            status="Planned",
            remarks="Morning yoga session"
        )
        update_url = reverse("activity-update", kwargs={"pk": activity.pk})

        for new_status in ["In-Progress", "Completed", "Planned"]:
            response = self.client.patch(update_url, {"status": new_status}, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data["status"], new_status)

    def test_delete_activity(self):
        activity = Activity.objects.create(
            user=self.user,
            activity_type="Boxing",
            date_time=timezone.now(),
            duration=timedelta(minutes=30),
            status="Planned",
            remarks="Incorrect entry"
        )
        delete_url = reverse("activity-delete", kwargs={"pk": activity.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Confirm it's gone
        detail_url = reverse("activity-detail", kwargs={"pk": activity.pk})
        follow_up = self.client.get(detail_url)
        self.assertEqual(follow_up.status_code, status.HTTP_404_NOT_FOUND)