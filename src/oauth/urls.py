from django.urls import path
from .views import *

urlpatterns = [
    path('login/', TokenObtainView.as_view(), name='login'),
]