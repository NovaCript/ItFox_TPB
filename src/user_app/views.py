from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, exceptions
from . import serializers

User = get_user_model()


class UserCreate(viewsets.ModelViewSet):
    """
    Cоздание пользователя.
    """
    serializer_class = serializers.UserSerializer
    permissions_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class UserView(viewsets.ModelViewSet):
    """
    Просмотр редактирование данных пользователя.
    """
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user