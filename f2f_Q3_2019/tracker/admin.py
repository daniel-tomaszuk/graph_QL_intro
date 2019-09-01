from django.contrib import admin

# Register your models here.
from tracker.models import Position, Satellite


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Satellite)
class SatelliteAdmin(admin.ModelAdmin):
    pass
