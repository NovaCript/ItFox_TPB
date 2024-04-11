from django.urls import path
from . import views

urlpatterns = [
    path('my-news/', views.NewsAuthorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('my-news/<int:pk>', views.NewsAuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', views.NewsViewSet.as_view({'get': 'list'})),
    path('<int:pk>', views.NewsViewSet.as_view({'get':'retrieve'})),
]