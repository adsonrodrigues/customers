from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from clients.models import Profile
from api.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
