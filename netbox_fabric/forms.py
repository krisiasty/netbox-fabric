from django import forms

from dcim.models import Region
from netbox.forms import NetBoxModelFilterSetForm, NetBoxModelForm
from utilities.forms.fields import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    SlugField,
    TagFilterField,
)
from utilities.forms.rendering import FieldSet

from .models import Fabric


class FabricForm(NetBoxModelForm):
    region = DynamicModelChoiceField(
        queryset=Region.objects.all(),
    )
    slug = SlugField()

    class Meta:
        model = Fabric
        fields = ("region", "name", "slug", "fabric_number", "description", "tags")


class FabricFilterForm(NetBoxModelFilterSetForm):
    model = Fabric
    fieldsets = (
        FieldSet(
            "q",
            "filter_id",
            "tag",
        ),
        FieldSet(
            "region_id",
            "fabric_number",
            name="Attributes",
        ),
    )

    region_id = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label="Region",
    )
    fabric_number = forms.IntegerField(
        required=False,
    )
    tag = TagFilterField(model)
