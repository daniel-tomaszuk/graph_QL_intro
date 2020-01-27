from django.contrib import admin

# Register your models here.
from tracker.models import Position
from tracker.models import Satellite


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Satellite)
class SatelliteAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
