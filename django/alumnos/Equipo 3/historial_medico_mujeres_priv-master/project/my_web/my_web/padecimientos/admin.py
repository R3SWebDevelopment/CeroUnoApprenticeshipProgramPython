from django.contrib import admin

from .models import Padecimiento
from .forms import PadecimientoForm

class PadecimientoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_padecimiento",
        "intensidad_padecimiento"
    ]

    form = PadecimientoForm

    search_fields = [
        "nombre_padecimiento"
    ]

    list_filter = [
        "intensidad_padecimiento"
    ]


admin.site.register(Padecimiento,PadecimientoAdmin)