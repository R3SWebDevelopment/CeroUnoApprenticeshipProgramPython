from django.contrib import admin

from .models import Diagnostico
from .forms import DiagnosticoForm

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = [
        "id_diagnostico",
        "fecha_diagnostico",
        "historial_diagnostico",
        "doctor_emite_diagnostico",
    ]

    form = DiagnosticoForm

    search_fields = [
        "doctor_emite_diagnostico"
    ]

    list_filter = [
        "fecha_diagnostico",
        "doctor_emite_diagnostico"
    ]

admin.site.register(Diagnostico,DiagnosticoAdmin)