from netbox.api.routers import NetBoxRouter

from . import views


app_name = "netbox_fabric"

router = NetBoxRouter()
router.register("fabrics", views.FabricViewSet)

urlpatterns = router.urls
