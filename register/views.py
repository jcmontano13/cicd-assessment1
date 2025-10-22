from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import CustomUser

@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        CustomUser.objects.filter(email=email).delete()
        return JsonResponse({"message": "User deleted"}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)
from django.shortcuts import render

# Create your views here.
