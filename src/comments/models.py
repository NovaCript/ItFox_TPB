from django.db import models
from django.contrib.auth import get_user_model
from ..news.models import News

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="news_comments",
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"ID: {self.id}, Author: {self.author}, Created at: {created_at_str}, News: {self.news.title}"
