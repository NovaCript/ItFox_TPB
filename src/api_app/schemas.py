from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ItFox-News",
        default_version='v1',
        description="Тестовое задание для ItFox на Django Rest Framework",
        contact=openapi.Contact(url="https://github.com/NovaCript"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)