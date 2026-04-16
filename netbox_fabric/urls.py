from django.urls import include, path
from utilities.urls import get_model_urls


urlpatterns = (
    path(
        "fabrics/",
        include(get_model_urls("netbox_fabric", "fabric", detail=False)),
    ),
    path(
        "fabrics/<int:pk>/",
        include(get_model_urls("netbox_fabric", "fabric")),
    ),
)
