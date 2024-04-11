from django.urls import path
from .views import *

urlpatterns = [
    path('me/', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('register/', UserCreate.as_view({'post': 'create'})),
]