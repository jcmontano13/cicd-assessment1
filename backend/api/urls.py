from django.urls import path
from .views import register_user, health_check, LoginView

urlpatterns = [
    path('register/', register_user, name='register'),  # ✅ matches reverse('register')
    path('health/', health_check),
    path('login/', LoginView.as_view(), name='login'),  # ✅ new login endpoint
]