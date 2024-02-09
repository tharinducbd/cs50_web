from django.db import models


# Create your models here.
class Material(models.Model):
    material_name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.material_name}"


class Tank(models.Model):
    capacity = models.IntegerField()
    construction_material = models.ForeignKey(Material,
                                             on_delete=models.CASCADE,
                                             related_name="tank_materials")
    color = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f"{self.id}: {self.capacity}"
