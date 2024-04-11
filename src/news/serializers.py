from rest_framework import serializers
from.models import *



class NewsSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'author', 'author_username', 'created_at')
        extra_kwargs = {
            'author': {'read_only': True},
            'created_at': {'read_only': True},
        }

    def get_author_username(self, obj):
        return obj.author.username