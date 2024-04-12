from django.urls import path
from .views import LikeViewSet


urlpatterns = [
    path(
        "news/<int:news_id>/like/",
        LikeViewSet.as_view({"post": "create", "delete": "destroy"}),
    ),
]
