from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowViewSet
)

# Инициализация роутера для ViewSets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

# Основные URL-паттерны API
urlpatterns = [
    # API v1
    path('v1/', include(router.urls)),

    # Эндпоинт для подписок (отдельный, т.к. использует mixins)
    path(
        'v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='follow'
    ),

    # JWT-аутентификация
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Эндпоинт для проверки работы API (опционально)
    path('v1/auth/', include('djoser.urls')),
]
