from django.core.exceptions import ValidationError
from django.test import TestCase

from dcim.models import Region

from netbox_fabric.models import Fabric


class FabricModelTestCase(TestCase):
    def setUp(self):
        self.region_one = Region.objects.create(name="Region A", slug="region-a")
        self.region_two = Region.objects.create(name="Region B", slug="region-b")

    def test_name_is_unique_within_region(self):
        Fabric.objects.create(
            region=self.region_one,
            name="Spine Fabric",
            slug="spine-fabric-a",
            fabric_number=100,
        )

        fabric = Fabric(
            region=self.region_one,
            name="Spine Fabric",
            slug="spine-fabric-b",
            fabric_number=200,
        )

        with self.assertRaises(ValidationError):
            fabric.full_clean()

    def test_slug_is_unique_within_region(self):
        Fabric.objects.create(
            region=self.region_one,
            name="Spine Fabric",
            slug="shared-slug",
            fabric_number=100,
        )

        fabric = Fabric(
            region=self.region_one,
            name="Leaf Fabric",
            slug="shared-slug",
            fabric_number=200,
        )

        with self.assertRaises(ValidationError):
            fabric.full_clean()

    def test_fabric_number_is_unique_within_region(self):
        Fabric.objects.create(
            region=self.region_one,
            name="Spine Fabric",
            slug="spine-fabric",
            fabric_number=100,
        )

        fabric = Fabric(
            region=self.region_one,
            name="Leaf Fabric",
            slug="leaf-fabric",
            fabric_number=100,
        )

        with self.assertRaises(ValidationError):
            fabric.full_clean()

    def test_constraints_are_scoped_to_region(self):
        Fabric.objects.create(
            region=self.region_one,
            name="Shared Fabric",
            slug="shared-fabric",
            fabric_number=100,
        )

        fabric = Fabric(
            region=self.region_two,
            name="Shared Fabric",
            slug="shared-fabric",
            fabric_number=100,
        )

        fabric.full_clean()
