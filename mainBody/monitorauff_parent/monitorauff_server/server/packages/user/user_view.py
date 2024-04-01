from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .user_model import User
from .user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
