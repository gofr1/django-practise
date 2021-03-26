from uuid import uuid4

from functools import lru_cache
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    @property
    def is_writer(self):
        return self.user.groups.filter(name='writer').exists()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    text = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(max_length=32, default=uuid4, unique=True, db_index=True)

    def __str__(self):
        return f'{self.author}: {self.created}: id {self.pk}'