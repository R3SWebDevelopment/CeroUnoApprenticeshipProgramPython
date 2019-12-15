from django.contrib import admin

from .models import Enfermedad
from .forms import EnfermedadForm

class EnfermedadAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_enfermedad",
        "enfermedad_mortal",
        "fecha_deteccion",
        "fecha_alta_paciente"
    ]

    form = EnfermedadForm

    search_fields = [
        "nombre_enfermedad"
    ]

    list_filter = [
        "enfermedad_mortal",
        "fecha_deteccion"
    ]

admin.site.register(Enfermedad, EnfermedadAdmin)