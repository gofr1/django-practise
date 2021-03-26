from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny

from .models import Post
from .serializers import PostSerializer


class IsAuthorReadOnly(BasePermission):
    """only authors should read posts"""

    def has_permission(self, request, view):
        if request.user.is_authenticated is not True:
            return False
        return request.method in SAFE_METHODS and request.user.profile.is_writer is True


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    permission_classes = [AllowAny]
