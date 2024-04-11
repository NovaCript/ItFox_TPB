from rest_framework import viewsets, permissions
from . import serializers
from ..base.permissions import IsAuthor
from .models import Comment
from ..base.paginations import CustomPagination


class ComentAuthorView(viewsets.ModelViewSet):
    """
    CRUD comments
    """

    serializer_class = serializers.AuthorCommentSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentView(viewsets.ModelViewSet):
    """
    Comments News
    """
    serializer_class = serializers.CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Comment.objects.filter(news=self.kwargs.get('pk'))