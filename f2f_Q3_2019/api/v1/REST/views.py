from django.db.models import Prefetch
from rest_framework import viewsets

from api.v1.REST.enums import PeriodQueryParamsEnums
from api.v1.REST.serializers import SatelliteSerializer
from tracker.models import Position
from tracker.models import Satellite


class SatellitePositionsView(viewsets.ModelViewSet):
    serializer_class = SatelliteSerializer

    def get_queryset(self):
        prefetch = Prefetch("positions", to_attr="satellite_positions")
        query_params = self.request.query_params.get("query", "")
        if query_params and query_params != PeriodQueryParamsEnums.ALL.value:
            # prepare query param - make it uppercase and snake case it
            query_params = query_params.upper().replace("-", "_")
            # filter query
            try:
                from_datetime, to_datetime = PeriodQueryParamsEnums[query_params].value
                prefetch = Prefetch(
                    "positions",
                    queryset=Position.objects.filter(
                        timestamp__gte=from_datetime, timestamp__lte=to_datetime,
                    ).order_by("-timestamp"),
                    to_attr="satellite_positions",
                )
            except KeyError:
                pass

        queryset = Satellite.objects.all().prefetch_related(prefetch)
        return queryset
