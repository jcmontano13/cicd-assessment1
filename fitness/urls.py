from django.urls import path
from .views import (
    ActivityCreateView,
    ActivityListView,
    ActivityDetailView,
    ActivityUpdateView,
    ActivityDeleteView
)


urlpatterns = [
    path("activity/", ActivityCreateView.as_view(), name="activity-create"),
    path("activity/list/", ActivityListView.as_view(), name="activity-list"),
    path("activity/<int:pk>/", ActivityDetailView.as_view(), name="activity-detail"),
    path("activity/update/<int:pk>/", ActivityUpdateView.as_view(), name="activity-update"),  # 👈 New
    path("activity/delete/<int:pk>/", ActivityDeleteView.as_view(), name="activity-delete"),
]

