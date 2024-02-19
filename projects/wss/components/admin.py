from django.contrib import admin

from .models import Material, Tank, Scheme, TreatmentProcess


class TankAdmin(admin.ModelAdmin):
    list_display = ("capacity", "construction_material", "has_bulkmeter")

class SchemeAdmin(admin.ModelAdmin):
    filter_horizontal = ("list_treatments",)

# Register your models here.
admin.site.register(Material)
admin.site.register(Tank, TankAdmin)
admin.site.register(TreatmentProcess)
admin.site.register(Scheme, SchemeAdmin)
