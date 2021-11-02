from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from ..models.title import Title
from ..permissions import IsOwnerOrReadOnly
from ..serializers.review import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id'),
        )
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id'),
        )
        return title.review.all()
