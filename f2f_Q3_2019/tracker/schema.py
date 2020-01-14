import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from tracker.models import Position
from tracker.models import Satellite


class SatelliteNode(DjangoObjectType):
    class Meta:
        model = Satellite
        fields = [
            "name",
            "norad_id",
            "positions",
        ]  # `fields` or `exclude`, `__all__` can be used
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "norad_id": ["exact"],
        }
        interfaces = (graphene.relay.Node,)

    satellite_alias = graphene.String()

    def resolve_satellite_alias(self, info):
        return "This is satellite alias from GraphQL."


class PositionNode(DjangoObjectType):
    class Meta:
        model = Position
        filter_fields = {
            "satellite__name": ["exact", "icontains", "istartswith"],
            "timestamp": ["exact", "lte", "gte"],
        }
        interfaces = (graphene.relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.order_by("-timestamp")
        return queryset.order_by("-timestamp")


class Query(graphene.ObjectType):
    satellite = graphene.relay.Node.Field(SatelliteNode)
    all_satellites = DjangoFilterConnectionField(SatelliteNode)

    position = graphene.relay.Node.Field(PositionNode)
    all_positions = DjangoFilterConnectionField(PositionNode)
