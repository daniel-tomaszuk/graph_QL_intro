from django.db import models


class Satellite(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True, unique=True)
    norad_id = models.IntegerField(default=0)
    created = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return f'Satellite {self.name} | NORAD: {self.norad_id}'


class Position(models.Model):
    satellite = models.ForeignKey(Satellite, related_name='positions', on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    azimuth = models.FloatField(null=True, blank=True)
    elevation = models.FloatField(null=True, blank=True)
    ra = models.FloatField(null=True, blank=True)
    dec = models.FloatField(null=True, blank=True)

    observer_altitude = models.FloatField(null=True, blank=True)
    observer_latitude = models.FloatField(null=True, blank=True)
    observer_longitude = models.FloatField(null=True, blank=True)

    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return f'Position for Satellite {self.satellite.name} | LAT: ' \
               f'{self.latitude}, LONG: {self.longitude}, ALT: {self.altitude}'
