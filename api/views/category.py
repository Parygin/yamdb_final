from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from ..models.category import Category
from ..permissions import IsStaffOrReadOnly
from ..serializers.category import CategorySerializer
from .mixins import MixinViewSet


class CategoryViewSet(MixinViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    pagination_class = PageNumberPagination
