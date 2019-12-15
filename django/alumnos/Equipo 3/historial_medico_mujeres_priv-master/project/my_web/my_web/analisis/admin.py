from django.contrib import admin

from .models import Analisis
from .forms import AnalisisForm

class AnalisisAdmin(admin.ModelAdmin):
    list_display = [
        'tipo_analisis',
        'fecha_de_solicitud',
        'fecha_resultados',
        'analisis_del_diagnostico',
    ]

    form = AnalisisForm

    search_fields = [
        "fecha_de_solicitud",
        "fecha_resultados"
    ]

    list_filter = [
        "fecha_de_solicitud",
        "fecha_resultados"
    ]

admin.site.register(Analisis, AnalisisAdmin)