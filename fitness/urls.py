from django.urls import path
from .views import ActivityCreateView, ActivityListView

urlpatterns = [
    path("activity/", ActivityCreateView.as_view(), name="activity-create"),
    path("activity/list/", ActivityListView.as_view(), name="activity-list"),
]
