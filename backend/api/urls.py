from django.urls import path
from .views import register_user, health_check

urlpatterns = [
    path('register/', register_user, name='register'),  # ✅ matches reverse('register')
    path('health/', health_check),
]