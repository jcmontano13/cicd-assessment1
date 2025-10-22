from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginView

from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/login/', LoginView.as_view(), name="login"),

]

