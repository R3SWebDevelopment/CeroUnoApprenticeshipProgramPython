from django.contrib import admin

from .models import Historial
from .forms import HistorialForm

class HistorialAdmin(admin.ModelAdmin):
    list_display = [
        'clave_instituto',
        'fecha_creacion_historial',
        'mujer_historial'
    ]

    form = HistorialForm

    search_fields = [
        "mujer_historial__nombre",
        "mujer_historial__apellido_paterno",
        "mujer_historial__apellido_materno"
    ]

    list_filter = [
        "clave_instituto", "fecha_creacion_historial"
    ]
admin.site.register(Historial, HistorialAdmin)