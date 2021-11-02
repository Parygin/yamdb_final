from .category import CategoryViewSet
from .comment import CommentViewSet
from .genre import GenreViewSet
from .review import ReviewViewSet
from .title import TitleViewSet
from .user import CustomUserViewSet, email_request, get_token

__all__ = ['CategoryViewSet', 'CommentViewSet',
           'GenreViewSet', 'ReviewViewSet',
           'TitleViewSet', 'CustomUserViewSet',
           'email_request', 'get_token']
