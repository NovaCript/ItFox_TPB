from rest_framework import serializers
from .models import Comment
from ..user_app.serializers import UserSerializer


class AuthorCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "created_at",
            "author",
            "news",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "created_at",
            "author",
            "news",
        )
