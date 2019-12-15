from django.contrib import admin

from .models import Mujer
from .forms import MujerForm

class MujerAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "apellido_paterno",
        "paciente_enferma",
        "fecha_ultima_menstruacion"
    ]

    form = MujerForm

    search_fields = [  # Aqui definimos los campos que se utilizan para hacer busquedas
        "nombre", 'apellido_paterno',
    ]

    list_filter = [  # Aqui definimos los campos que se utilizan para hacer filtros
        'apellido_paterno', 'paciente_enferma',
    ]

admin.site.register(Mujer, MujerAdmin)