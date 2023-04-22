from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/create/', include('djoser.urls.jwt')),
    path('v1/jwt/refresh/', include('djoser.urls.jwt')),
    path('v1/jwt/verify/', include('djoser.urls.jwt')),
    path('v1/', include('djoser.urls.jwt')),
]
