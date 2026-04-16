from dcim.api.serializers import RegionSerializer
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ..models import Fabric


class FabricSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_fabric-api:fabric-detail",
    )
    region = RegionSerializer(
        nested=True,
    )

    class Meta:
        model = Fabric
        fields = (
            "id",
            "url",
            "display",
            "name",
            "slug",
            "fabric_number",
            "description",
            "region",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
        brief_fields = ("id", "url", "display", "name", "slug", "fabric_number")
