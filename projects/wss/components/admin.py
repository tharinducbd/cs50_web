from django.contrib import admin

from .models import Material, Tank, Scheme, TreatmentProcess

# Register your models here.
admin.site.register(Material)
admin.site.register(Tank)
admin.site.register(TreatmentProcess)
admin.site.register(Scheme)
