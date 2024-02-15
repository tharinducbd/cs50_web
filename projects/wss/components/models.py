from django.db import models


# Choices
BOOL_CHOICES = ((True, 'Yes'),(False, 'No'))
TREATMENT_TYPE = [
    ("PT_INT", "Pre-treatment: Intake"),
    ("PT_WTP", "Pre-treatment: WTP"),
    ("AE", "Aeration"),
    ("SF", "Sand Filtration"),
    ("DI", "Disinfection"),
    ("OTHER", "Other Treatment")
]


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


class TreatmentProcess(models.Model):
    treatment_type = models.CharField(max_length=100, choices=TREATMENT_TYPE, default="OTHER")
    process_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.process_name}"


class Scheme(models.Model):
    scheme_name = models.CharField(max_length=64)
    district = models.CharField(max_length=32)
    tanks = models.ManyToManyField(Tank, blank=True, related_name="schemes")
    treatment = models.ManyToManyField(TreatmentProcess, blank=True, related_name="schemes")

    def __str__(self) -> str:
        return f"{self.district} {self.scheme_name}"
