from rest_framework import viewsets

from api.v1.REST.enums import PeriodQueryParamsEnums
from api.v1.REST.serializers import SatelliteSerializer
from tracker.models import Satellite


class SatellitePositionsView(viewsets.ModelViewSet):
    serializer_class = SatelliteSerializer

    def get_queryset(self):
        queryset = Satellite.objects.prefetch_related("positions").all()
        query_params = self.request.query_params.get("query", "")
        if query_params and query_params != PeriodQueryParamsEnums.ALL.value:
            # prepare query param - make it uppercase and snake case it
            query_params = query_params.upper().replace("-", "_")
            # filter query
            try:
                from_datetime, to_datetime = PeriodQueryParamsEnums[query_params].value
                queryset = queryset.filter(
                    positions__timestamp__gte=from_datetime,
                    positions__timestamp__lte=to_datetime,
                )
            except KeyError:
                pass

        return queryset
