from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate
import json

from .models import CustomUser

@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            email = data.get("email")
            password = data.get("password")
            display_name = data.get("display_name")

            if not email or not password or not display_name:
                return JsonResponse({"error": "All fields are required"}, status=400)

            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already registered"}, status=400)

            user = CustomUser.objects.create_user(
                email=email,
                display_name=display_name,
                password=password,
            )

            return JsonResponse(
                {"message": "User registered successfully", "user_id": user.id},
                status=201,
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"error": "Email and password are required"}, status=400)

            user = authenticate(request, username=email, password=password)

            if user is not None:
                return JsonResponse({"message": "Login successful", "user_id": user.id}, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)