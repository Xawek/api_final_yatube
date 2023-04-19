from django.shortcuts import get_object_or_404
from posts.models import Group, Post, Follow
from rest_framework import permissions, viewsets, filters, pagination

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer,
                             GroupSerializer,
                             PostSerializer,
                             FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def perform_create(self, serializer):
        user_request = self.request.user
        return serializer.save(user=user_request)

    def get_queryset(self):
        user_request = self.request.user
        return Follow.objects.filter(user=user_request)
