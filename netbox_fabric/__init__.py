from netbox.plugins import PluginConfig


class NetBoxFabricConfig(PluginConfig):
    name = "netbox_fabric"
    verbose_name = "NetBox Fabric"
    description = "Model switching fabrics by region"
    version = "0.1.1"
    base_url = "netbox-fabric"
    min_version = "4.5.7"
    max_version = None


config = NetBoxFabricConfig
