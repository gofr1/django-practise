from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save

from rest_framework.test import APIClient

import pytest

from ..models import Post, Profile

import factory


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: f"Group {n}")


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory('app.factories.UserFactory', profile=None)


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"user_{n}d")
    profile = factory.RelatedFactory(ProfileFactory, 'user')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    text = factory.Sequence(lambda n: f"user_{n}")


@pytest.fixture
def author():
    author = UserFactory(
        email='kit@example.com', username='McKittens', password='dont tell Anyone'
    )
    Post(author=author, text='hey')

    content_type = ContentType.objects.get_for_model(Post)
    group = GroupFactory(name='writer')

    author.groups.add(group)

    return author


@pytest.fixture
def non_author():
    return UserFactory(
        email='kities@example.com', username='Kittass', password='dont tell Anyone'
    )
