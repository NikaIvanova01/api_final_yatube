from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', GroupViewSet, basename='groups')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='follow'
    ),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='jwt-create'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='jwt-refresh'
    ),
    path(
        'v1/jwt/verify/',
        TokenVerifyView.as_view(),
        name='jwt-verify'
    ),
]
