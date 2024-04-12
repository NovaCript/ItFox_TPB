from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .serializers import LikeSerializer
from .models import Like
from ..news.models import News


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Like.objects.filter(news=self.kwargs["news_id"])

    def create(self, request, *args, **kwargs):
        news_id = self.kwargs["news_id"]
        user = request.user
        news = News.objects.get(id=news_id)
        like, created = Like.objects.get_or_create(user=user, news=news)
        if created:
            return Response({"status": "Like!"}, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "Like already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        news_id = self.kwargs["news_id"]
        user = request.user
        news = News.objects.get(id=news_id)
        like = Like.objects.filter(user=user, news=news).first()
        if like:
            like.delete()
            return Response({"status": "Like deleted"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"status": "Like not found"}, status=status.HTTP_404_NOT_FOUND
            )
