from django.db import models
from django.contrib.auth import get_user_model


class Activity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.activity_type} on {self.date_time}"


from django.db import models

# Create your models here.
