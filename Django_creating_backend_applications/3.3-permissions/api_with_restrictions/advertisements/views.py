
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from advertisements import models
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
# from advertisements.permissons import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class =  AdvertisementFilter
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров


    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]  # Для создания объявления требуется аутентификация
        elif self.action in ["update", "partial_update"]:
            post_id = self.kwargs['pk']
            post = models.Advertisement.objects.get(id=post_id)
            if self.request.user == post.creator:
                return [IsAuthenticated()]  # Изменение объявления разрешено только его создателю
            return Response(status=status.HTTP_404_NOT_FOUND)
