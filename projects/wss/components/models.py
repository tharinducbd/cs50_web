from django.db import models


# Create your models here.
class Tank(models.Model):
    capacity = models.IntegerField()
    scheme_name = models.CharField(max_length=32)


class Material(models.Model):
    material = models.CharField(max_length=64)
