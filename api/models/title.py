import datetime

from django.core.exceptions import ValidationError
from django.db import models

from .category import Category
from .genre import Genre

NOW = datetime.datetime.now()


def validate_year(value):
    if value < 868 and value > NOW.year:
        raise ValidationError(
            ('%(value)s is not correct year.'),
            params={'value': value},
        )


class Title(models.Model):
    name = models.CharField(
        max_length=300,
        blank=False,
    )
    description = models.TextField(
        blank=True,
    )
    year = models.PositiveSmallIntegerField(
        validators=[validate_year],
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
