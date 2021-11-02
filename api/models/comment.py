from django.contrib.auth import get_user_model
from django.db import models

from .review import Review

User = get_user_model()


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
    )
    text = models.TextField(max_length=2000)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )
