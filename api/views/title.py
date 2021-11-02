import django_filters
from django.db.models import Avg
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from ..models.title import Title
from ..permissions import IsStaffOrReadOnly
from ..serializers.title import TitleListSerializer, TitleSerializer


class TitleFilter(filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name='genre__slug', lookup_expr='contains'
    )
    category = django_filters.CharFilter(
        field_name='category__slug', lookup_expr='contains'
    )
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='contains'
    )

    class Meta:
        model = Title
        fields = {
            'year': ['exact'],
        }


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('review__score')).all()
    pagination_class = PageNumberPagination
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleListSerializer
        return TitleSerializer
