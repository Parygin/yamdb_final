from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, CustomUserViewSet,
                    GenreViewSet, ReviewViewSet, TitleViewSet, email_request,
                    get_token)

v1_router = DefaultRouter()

v1_router.register('users', CustomUserViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('categories', CategoryViewSet)

v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='ReviewView',
)

v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='CommentView',
)

auth_patterns = [
    path('email/', email_request),
    path('token/', get_token),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(auth_patterns)),
]
