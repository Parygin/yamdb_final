from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from ..models.genre import Genre
from ..permissions import IsStaffOrReadOnly
from ..serializers.genre import GenreSerializer
from .mixins import MixinViewSet


class GenreViewSet(MixinViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    pagination_class = PageNumberPagination
