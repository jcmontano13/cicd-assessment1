from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer


class ActivityCreateView(generics.CreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from django.shortcuts import render

# Create your views here.
