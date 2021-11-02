from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField


class Membership(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
    )
    role = CharField(
        max_length=50,
        choices=Membership.choices,
        default=Membership.USER,
    )
    bio = models.TextField(blank=True)

    @property
    def is_moderator(self):
        return self.role == Membership.MODERATOR

    @property
    def is_admin(self):
        return (
            self.role == Membership.ADMIN
            or self.is_superuser
        )
