from rest_framework import viewsets

from api.v1.REST.serializers import SatelliteSerializer
from tracker.models import Satellite


class SatellitePositionsView(viewsets.ModelViewSet):
    queryset = Satellite.objects.prefetch_related("positions").all()
    serializer_class = SatelliteSerializer
