from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer


User = get_user_model()


class UserCreateViewSet(generics.CreateAPIView):
    model = User
    permission_classes = ()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserListViewSet(generics.ListAPIView):
    model = User
    permission_classes = ()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()