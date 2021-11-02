from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from .title import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review',
        blank=True,
        null=True,
    )
    text = models.TextField(
        max_length=5000,
        null=False,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True,
        null=True,
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1, message='Минимальное значение: "1"'),
            MaxValueValidator(10, message='Максимальное значение: "10"'),
        ),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        UniqueConstraint(fields=['author', 'title_id'], name='unique_pub')
