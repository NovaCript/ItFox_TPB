from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserCreateViewSet.as_view(), name='register'),
    path('all/', UserListViewSet.as_view(), name='users-list'),
]