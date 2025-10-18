from django.urls import path
from .views import register_user, LoginView

urlpatterns = [
    path('register/', register_user, name='register'),  # ✅ matches reverse('register')
    path('login/', LoginView.as_view(), name='login'),  # ✅ new login endpoint
]