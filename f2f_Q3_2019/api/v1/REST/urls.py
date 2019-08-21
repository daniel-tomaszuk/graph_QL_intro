from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.REST.views import SatellitePositionsView

router = DefaultRouter()
router.register(r'get-satellite-positions', SatellitePositionsView, basename='satellite-positions-rest')

urlpatterns = [path('v1/', include(router.urls))]
