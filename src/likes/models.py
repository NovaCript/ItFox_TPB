from django.contrib.auth import get_user_model
from django.db import models
from ..news.models import News


User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
