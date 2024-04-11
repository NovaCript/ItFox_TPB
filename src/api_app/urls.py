from django.urls import path, include

urlpatterns = [
    path('users/', include('src.user_app.urls')),
]