from django.db import models
from django.urls import reverse

from dcim.models import Region
from netbox.models import NetBoxModel


class Fabric(NetBoxModel):
    region = models.ForeignKey(
        to=Region,
        on_delete=models.PROTECT,
        related_name="fabrics",
    )
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(
        max_length=100,
    )
    fabric_number = models.PositiveIntegerField()
    description = models.CharField(
        max_length=500,
        blank=True,
    )

    class Meta:
        ordering = ("region", "fabric_number", "name")
        verbose_name = "Fabric"
        constraints = (
            models.UniqueConstraint(
                fields=("region", "name"),
                name="netbox_fabric_region_name_unique",
            ),
            models.UniqueConstraint(
                fields=("region", "slug"),
                name="netbox_fabric_region_slug_unique",
            ),
            models.UniqueConstraint(
                fields=("region", "fabric_number"),
                name="netbox_fabric_region_number_unique",
            ),
        )

    def __str__(self):
        return f"{self.region} / {self.name}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_fabric:fabric", args=[self.pk])
