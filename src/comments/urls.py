from django.urls import path
from . import views

urlpatterns = [
    path('my_comments/', views.ComentAuthorView.as_view({'get': 'list', 'post': 'create'})),
    path('my_comments/<int:pk>/', views.ComentAuthorView.as_view({'get':'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('comment_by_news/<int:pk>/', views.CommentView.as_view({'get': 'list'})),
    path('comment_by_news/<int:pk>/<int:comment_pk>/delete/', views.CommentView.as_view({'delete': 'destroy'})),
]