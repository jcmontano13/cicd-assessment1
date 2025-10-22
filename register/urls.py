# register/urls.py
from django.urls import path
from .views import delete_user  # Add other views here as needed

urlpatterns = [
    path('delete-user/', delete_user),
]
