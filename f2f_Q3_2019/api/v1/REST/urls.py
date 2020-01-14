from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.REST.views import SatellitePositionsView

router = DefaultRouter()
router.register(
    r"get-satellite-positions",
    SatellitePositionsView,
    basename="satellite-positions-rest",
)

urlpatterns = [path("", include(router.urls))]
