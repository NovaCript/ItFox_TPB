from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "All News"

    def __str__(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"ID: {self.id}, Tile: {self.title}, Author: {self.author}, Created at: {created_at_str}"
