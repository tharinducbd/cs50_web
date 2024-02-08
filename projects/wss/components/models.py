from django.db import models


# Create your models here.
class Tank(models.Model):
    capacity = models.IntegerField()
    scheme_name = models.CharField(max_length=64)
    tank_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.id}: {self.tank_name} of {self.scheme_name} - {self.capacity}"


class Material(models.Model):
    material = models.CharField(max_length=64)
