from rest_framework import serializers

from tracker.models import Position
from tracker.models import Satellite


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["latitude", "longitude"]


class SatelliteSerializer(serializers.ModelSerializer):
    satellite_positions = PositionSerializer(many=True, read_only=True)

    class Meta:
        model = Satellite
        fields = ["name", "norad_id", "satellite_positions"]
