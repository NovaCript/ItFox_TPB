from rest_framework import viewsets, permissions, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import serializers
from ..base.permissions import IsAdminOrAuthor
from .models import Comment
from ..base.paginations import CustomPagination


class ComentAuthorView(viewsets.ModelViewSet):
    """
    CRUD comments
    """

    serializer_class = serializers.AuthorCommentSerializer
    permission_classes = [IsAdminOrAuthor]

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
        return Comment.objects.filter(news=self.kwargs.get("pk"))

    def get_object(self):
        comment = get_object_or_404(Comment, pk=self.kwargs["comment_pk"])
        if comment.news.author != self.request.user:
            raise exceptions.PermissionDenied(
                "You do not have permission to delete this comment."
            )
        self.check_object_permissions(self.request, comment)
        return comment

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        self.perform_destroy(comment)
        return Response(status=status.HTTP_204_NO_CONTENT)
