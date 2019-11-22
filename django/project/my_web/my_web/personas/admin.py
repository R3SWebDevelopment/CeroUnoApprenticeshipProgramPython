from django.contrib import admin

from .models import (
    Persona,
    Hermandad,
    Miembro,
)
from .forms import (
    PersonaForm,
    HermandadForm,
    HermandadFormSet,
    MiembroForm,
)


class HermanoTabularAdmin(admin.TabularInline):
    model = Hermandad
    extra = 0
    form = HermandadForm
    formset = HermandadFormSet
    fk_name = 'persona_uno'


class PersonaTabularAdmin(admin.TabularInline):
    model = Persona
    extra = 0
    max_num = 1
    form = PersonaForm


class PadreTabularAdmin(PersonaTabularAdmin):
    fk_name = 'padre'
    verbose_name = 'Padre'
    verbose_name_plural = "Padre"


class MadreTabularAdmin(PersonaTabularAdmin):
    fk_name = 'madre'
    verbose_name = 'Madre'
    verbose_name_plural = "Madre"


class ParejaTabularAdmin(PersonaTabularAdmin):
    fk_name = 'pareja'
    verbose_name = 'Pareja'
    verbose_name_plural = "Pareja"


def enroll_persona_membresia(modeladmin, request, queryset):
    for persona in queryset:
        if not persona.is_member:
            Miembro.enroll_persona(persona=persona)


enroll_persona_membresia.short_description = "Inscribir Miembro"


class PersonaAdmin(admin.ModelAdmin):
    list_display = [  # Aqui definimos los campos que se muestran en el listado de personas
        'nombre', 'apellido_paterno', 'genero', 'tiene_pareja', 'tiene_padre', 'tiene_madre', 'tiene_hermanos',
        'es_miembro',
    ]
    search_fields = [  # Aqui definimos los campos que se utilizan para hacer busquedas
        "nombre", 'apellido_paterno',
    ]
    list_filter = [  # Aqui definimos los campos que se utilizan para hacer filtros
        'apellido_paterno', 'genero',
    ]
    form = MiembroForm

    inlines = [
        PadreTabularAdmin,
        MadreTabularAdmin,
        ParejaTabularAdmin,
        HermanoTabularAdmin,
    ]
    actions = [enroll_persona_membresia]

    def tiene_pareja(self, obj):
        return obj.tiene_pareja

    def tiene_padre(self, obj):
        return obj.tiene_padre

    def tiene_madre(self, obj):
        return obj.tiene_madre

    def tiene_hermanos(self, obj):
        return obj.tiene_hermanos

    def es_miembro(self, obj):
        return obj.is_member


admin.site.register(Persona, PersonaAdmin)


class MiembroAdmin(PersonaAdmin):
    list_display = PersonaAdmin.list_display
    list_filter = PersonaAdmin.list_filter


admin.site.register(Miembro, MiembroAdmin)
