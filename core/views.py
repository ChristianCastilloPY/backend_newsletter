from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.state import User

from core.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer
