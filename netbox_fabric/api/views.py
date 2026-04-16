from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import FabricSerializer


class FabricViewSet(NetBoxModelViewSet):
    queryset = models.Fabric.objects.select_related("region").prefetch_related("tags")
    serializer_class = FabricSerializer
    filterset_class = filtersets.FabricFilterSet
