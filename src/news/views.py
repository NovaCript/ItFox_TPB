from rest_framework import viewsets, permissions, exceptions
from .models import News
from . import serializers
from ..base.permissions import IsAdminOrAuthor
from ..base.paginations import CustomPagination


class NewsAuthorViewSet(viewsets.ModelViewSet):
    """
    CRUD for News
    """

    permission_classes = [IsAdminOrAuthor]
    serializer_class = serializers.AuthorNewsSerializer

    def get_queryset(self):
        return News.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class NewsViewSet(viewsets.ModelViewSet):
    """
    All News
    """

    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_serializer_context(self):
        return {"request": self.request}
