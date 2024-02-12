from django.db import models


# Yes/ No for boolean selects.
BOOL_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


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
    has_ball_valve = models.BooleanField(choices=BOOL_CHOICES, default=False)
    has_overflow = models.BooleanField(choices=BOOL_CHOICES, default=False)
    has_washout = models.BooleanField(choices=BOOL_CHOICES, default=False)
    has_chamber = models.BooleanField(choices=BOOL_CHOICES, default=False)
    has_bulkmeter = models.BooleanField(choices=BOOL_CHOICES, default=False)
    

    def __str__(self) -> str:
        return f"{self.id}: {self.capacity}m3 {self.construction_material}"
