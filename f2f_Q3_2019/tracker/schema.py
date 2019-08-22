import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from tracker.models import Satellite, Position


class SatelliteNode(DjangoObjectType):
    class Meta:
        model = Satellite
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'norad_id': ['exact']
        }
        interfaces = (graphene.relay.Node,)


class PositionNode(DjangoObjectType):
    class Meta:
        model = Position
        filter_fields = {
            'satellite__name': ['exact', 'icontains', 'istartswith'],
            'timestamp': ['exact']
        }
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    satellite = graphene.relay.Node.Field(SatelliteNode)
    all_satellites = DjangoFilterConnectionField(SatelliteNode)

    position = graphene.relay.Node.Field(PositionNode)
    all_positions = DjangoFilterConnectionField(PositionNode)
