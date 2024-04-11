from rest_framework import serializers
from .models import *
from ..user_app.serializers import UserSerializer


class AuthorNewsSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author_username",
            "created_at",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def get_author_username(self, obj):
        return obj.author.username


class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author",
            "created_at",
            "news_comments",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def get_author_username(self, obj):
        return obj.author.username
