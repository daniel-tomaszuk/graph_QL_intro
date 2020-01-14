from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("api/v1/REST/", include("api.v1.REST.urls")),
    path("api/v1/GRAPH/", include("api.v1.GRAPH.urls")),
    path("satellite-map/", include("tracker.urls")),
    path("admin/", admin.site.urls),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)  # TODO: fix it.
