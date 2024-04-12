from django.urls import path, include
from .schemas import schema_view


urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("users/", include("src.user_app.urls")),
    path("auth/", include("src.oauth.urls")),
    path("news/", include("src.news.urls")),
    path("comments/", include("src.comments.urls")),
    path("like/", include("src.likes.urls")),
]
