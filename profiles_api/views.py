from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers, models

class UserProfileViewSet(viewsets.ModelViewSet):
    """Viewset for interfacing with UserProfile model"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    