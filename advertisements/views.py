from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_with_restrictions.permissions import IsOwner

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    filterset_fields = ['creator', 'status']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
        
