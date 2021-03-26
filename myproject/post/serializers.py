from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        lookup_field = 'slug'
        fields = ['author', 'text', 'created']

    created = serializers.DateTimeField(format='%a, %d %b %Y')
    author = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
