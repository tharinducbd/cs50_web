from django.db import models


INTERVALS = [
    ("DAILY", "Daily"), ("WEEKLY", "Weekly"), ("FORTNIGHTLY", "Fortnightly"),
    ("MONTHLY", "Monthly"), ("QUATERLY", "Quarterly"),
    ("BIANNUALLY", "Biannually"), ("ANNUALLY", "Annually")
]
RESPONSIBILITY = [
    ("CT", "Caretaker(s)"),
    ("CBO", "Community Organization"),
    ("LA", "Local Agent")
]


class Component_Type(models.Model):
    component_type = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.component_type.capitalize()}"

    class Meta:
        verbose_name = "Component Type"
        verbose_name_plural = "Component Types"


class Component(models.Model):
    component_type = models.ForeignKey(Component_Type,
                                       on_delete=models.CASCADE,
                                       related_name="components")
    component = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"Component: {self.component.capitalize()}, Type: {self.component_type.capitalize()}"


class Task(models.Model):
    task_name = models.CharField(max_length = 128)
    task_responsibility = models.CharField(max_length=32, choices=RESPONSIBILITY, default="CT")
    task_interval = models.CharField(max_length=32, choices=INTERVALS, default="DAILY")
    component = models.ManyToManyField(Component, blank=True, related_name="tasks")

    def __str__(self) -> str:
        return f"{self.task_name.capitalize()} - {self.task_interval} by {self.task_responsibility}"
