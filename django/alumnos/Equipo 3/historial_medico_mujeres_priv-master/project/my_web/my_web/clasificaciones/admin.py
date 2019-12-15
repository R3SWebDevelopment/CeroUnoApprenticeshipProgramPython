from django.contrib import admin

from .models import Clasificacion
from .forms import ClasificacionForm

class ClasificacionAdmin(admin.ModelAdmin):
    list_display = [
        "clasificacion_nombre",
        "tipo_enfermedad"
    ]

    form = ClasificacionForm

    search_fields = [
        "clasificacion_nombre",
        "tipo_enfermedad"
    ]

    list_filter = [
        "clasificacion_nombre",
        "tipo_enfermedad"
    ]

admin.site.register(Clasificacion, ClasificacionAdmin)