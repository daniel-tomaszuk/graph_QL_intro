import graphene
from graphene_django import DjangoObjectType

from tracker.models import Satellite, Position


class SatelliteType(DjangoObjectType):
    class Meta:
        model = Satellite


class PositionType(DjangoObjectType):
    class Meta:
        model = Position


class Query:
    satellite = graphene.Field(
        SatelliteType,
        id=graphene.Int(),
        norad_id=graphene.Int()
    )
    all_satellites = graphene.List(
        SatelliteType
    )

    position = graphene.Field(
        PositionType,
        id=graphene.Int()
    )
    all_positions = graphene.List(
        PositionType
    )

    def resolve_position(self, info, **kwargs):
        position_id = kwargs.get('id')
        if position_id:
            return Position.objects.get(id=position_id)
        return None

    def resolve_all_positions(self, info, **kwargs):
        return Position.objects.select_related('satellite').all()

    def resolve_satellite(self, info, **kwargs):
        satellite_id = kwargs.get('id')
        satellite_norad_id = kwargs.get('norad_id')
        if satellite_id:
            return Satellite.objects.get(id=satellite_id)
        if satellite_norad_id:
            return Satellite.objects.get(norad_id=satellite_norad_id)
        return None

    def resolve_all_satellites(self, info, **kwargs):
        return Satellite.objects.all()
