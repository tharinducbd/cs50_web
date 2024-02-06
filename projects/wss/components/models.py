from django.db import models


# Create your models here.
class Tank(models.Model):
    capacity = models.IntegerField()
    tank_type = models.CharField(max_length=32)


class Material(models.Model):
    material = models.CharField(max_length=64)
