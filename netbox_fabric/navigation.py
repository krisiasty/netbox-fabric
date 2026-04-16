from netbox.choices import ButtonColorChoices
from netbox.plugins import PluginMenuButton, PluginMenuItem


fabric_buttons = (
    PluginMenuButton(
        link="plugins:netbox_fabric:fabric_add",
        title="Add fabric",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
        permissions=["netbox_fabric.add_fabric"],
    ),
)

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_fabric:fabric_list",
        link_text="Fabrics",
        buttons=fabric_buttons,
    ),
)
