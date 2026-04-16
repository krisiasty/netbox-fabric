from netbox.views import generic
from utilities.views import register_model_view

from . import filtersets, forms, models, tables


@register_model_view(models.Fabric)
class FabricView(generic.ObjectView):
    queryset = models.Fabric.objects.select_related("region").prefetch_related("tags")


@register_model_view(models.Fabric, name="list", path="", detail=False)
class FabricListView(generic.ObjectListView):
    queryset = models.Fabric.objects.select_related("region").prefetch_related("tags")
    table = tables.FabricTable
    filterset = filtersets.FabricFilterSet
    filterset_form = forms.FabricFilterForm


@register_model_view(models.Fabric, name="add", detail=False)
@register_model_view(models.Fabric, name="edit")
class FabricEditView(generic.ObjectEditView):
    queryset = models.Fabric.objects.select_related("region").prefetch_related("tags")
    form = forms.FabricForm


@register_model_view(models.Fabric, name="delete")
class FabricDeleteView(generic.ObjectDeleteView):
    queryset = models.Fabric.objects.all()
