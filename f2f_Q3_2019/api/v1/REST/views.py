from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.tasks import get_satellite_positions


class SatellitePositionsView(ViewSet):

    def list(self, request):
        get_satellite_positions()
        return Response(status=status.HTTP_200_OK)
