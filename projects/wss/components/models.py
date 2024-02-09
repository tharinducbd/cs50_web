from django.db import models


# Create your models here.
class Material(models.Model):
    material = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.material}"


class Tank(models.Model):
    capacity = models.IntegerField()
    contruction_material = models.ForeignKey(Material,
                                             on_delete=models.CASCADE,
                                             related_name="tank_materials")

    def __str__(self) -> str:
        return f"{self.id}: {self.capacity}"
