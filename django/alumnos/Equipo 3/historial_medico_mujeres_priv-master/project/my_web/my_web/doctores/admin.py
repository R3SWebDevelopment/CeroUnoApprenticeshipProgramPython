from django.contrib import admin

from .models import Doctor
from .forms import DoctorForm

class DoctorAdmin(admin.ModelAdmin):
    list_display =  [
        "nombre_doctor",
        "cedula_doctor",
        "direccion_doctor",
    ]

    form = DoctorForm

    search_fields = [
        "nombre_doctor",
        "cedula_doctor"
    ]
    

admin.site.register(Doctor, DoctorAdmin)