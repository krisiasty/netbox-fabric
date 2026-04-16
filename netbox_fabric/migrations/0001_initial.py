import django.db.models.deletion
import netbox.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dcim", "0224_add_comments_to_organizationalmodel"),
        ("extras", "0134_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fabric",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                ("fabric_number", models.PositiveIntegerField()),
                ("description", models.CharField(blank=True, max_length=500)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="fabrics",
                        to="dcim.region",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
                ),
            ],
            options={
                "verbose_name": "Fabric",
                "ordering": ("region", "fabric_number", "name"),
            },
            bases=(netbox.models.deletion.DeleteMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name="fabric",
            constraint=models.UniqueConstraint(
                fields=("region", "name"),
                name="netbox_fabric_region_name_unique",
            ),
        ),
        migrations.AddConstraint(
            model_name="fabric",
            constraint=models.UniqueConstraint(
                fields=("region", "slug"),
                name="netbox_fabric_region_slug_unique",
            ),
        ),
        migrations.AddConstraint(
            model_name="fabric",
            constraint=models.UniqueConstraint(
                fields=("region", "fabric_number"),
                name="netbox_fabric_region_number_unique",
            ),
        ),
    ]
