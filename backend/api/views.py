from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from django.http import JsonResponse

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def health_check(request):
    return JsonResponse({"status": "ok"})