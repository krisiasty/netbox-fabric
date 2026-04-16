import django_tables2 as tables

from netbox.tables import NetBoxTable

from .models import Fabric


class FabricTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )
    region = tables.Column(
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = Fabric
        fields = (
            "pk",
            "id",
            "name",
            "slug",
            "fabric_number",
            "region",
            "description",
            "actions",
        )
        default_columns = (
            "name",
            "fabric_number",
            "region",
            "description",
            "actions",
        )
