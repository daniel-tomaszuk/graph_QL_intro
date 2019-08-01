from django.db import models

# Create your models here.


class Satellite(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True, unique=True)
    created = models.DateTimeField(db_index=True, auto_now_add=True)


class Position(models.Model):
    satellite = models.ForeignKey(Satellite, related_name='positions', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
