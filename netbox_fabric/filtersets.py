import django_filters
from django.db.models import Q

from dcim.models import Region
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filtersets import register_filterset

from .models import Fabric


@register_filterset
class FabricFilterSet(NetBoxModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    region_id = django_filters.ModelMultipleChoiceFilter(
        field_name="region",
        queryset=Region.objects.all(),
        label="Region",
    )

    class Meta:
        model = Fabric
        fields = ("id", "name", "slug", "fabric_number", "region_id")

    def search(self, queryset, name, value):
        value = value.strip()
        if not value:
            return queryset

        query = (
            Q(name__icontains=value)
            | Q(slug__icontains=value)
            | Q(description__icontains=value)
            | Q(region__name__icontains=value)
        )

        if value.isdigit():
            query |= Q(fabric_number=int(value))

        return queryset.filter(query)
