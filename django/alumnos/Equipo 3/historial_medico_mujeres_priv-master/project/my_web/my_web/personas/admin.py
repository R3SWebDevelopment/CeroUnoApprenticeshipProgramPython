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
    # Esta funcion es la que sera agregada al listado de acciones de PersonaAdmin
    # el parametro modeladmin hace referencia a un objeto de la clase PersonaAdmin
    # el parametro request hace referencia a la petición web invocada al hacer click al boton Go
    # el parametro queryset hace referencia al listado de objetos seleccionados en la lista de personas, al momento de
    # invocar la accion "Incribir Miembro"
    for persona in queryset:
        if not persona.is_member:
            Miembro.enroll_persona(persona=persona)


enroll_persona_membresia.short_description = "Inscribir Miembro"


class PersonaAdmin(admin.ModelAdmin):
    list_display = [  # Aqui definimos los campos que se muestran en el listado de personas
        'nombre',  # Esta campo viene del modelo Persona
        'apellido_paterno',  # Esta campo viene del modelo Persona
        'genero', 'tiene_pareja',   # Esta campo viene del modelo Persona
        # Los siguientes campos no se encuentran dentro del modelo Persona, entonces la clase PersonaAdmin los va a
        # buscar dentro de las propiedades y funciones contenidas en su propia clase
        'tiene_padre',
        'tiene_madre',
        'tiene_hermanos',
        'es_miembro',
    ]

    search_fields = [  # Aqui definimos los campos que se utilizan para hacer busquedas
        "nombre", 'apellido_paterno',
    ]
    list_filter = [  # Aqui definimos los campos que se utilizan para hacer filtros
        'apellido_paterno', 'genero',
    ]
    form = PersonaForm

    # En el atributo inlines, se definen todas aquellas clases que se utilizan para desplegar o capturar datos de manera
    # mas compleja, como aquellos datos que se encuentran en algun tipo de relación con la clase persona
    inlines = [
        PadreTabularAdmin,
        MadreTabularAdmin,
        ParejaTabularAdmin,
        HermanoTabularAdmin,
    ]
    # El atributo se definen todas aquellas funciones adicionales o hechas a la medida que afectaran a los registros
    # desplegados en el listado de personas
    actions = [enroll_persona_membresia]

    # Las siguientes funciones definidas, son las que utilizara la clase PersonaAdmin para deplegar información
    # calculada al vuelo en la lista de personas
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


def sign_up_member(modeladmin, request, queryset):
    pass


sign_up_member.short_description = "Dar Acceso al Portal"


class MiembroAdmin(PersonaAdmin):
    # La clase MiembroAdmin heredad de la clase PersonaAdmin, ya que sus funciones son similares, con esto se logra
    # reducir el numero de lineas de codigo y de metodos a implementar,
    list_display = PersonaAdmin.list_display
    list_filter = PersonaAdmin.list_filter
    actions = [sign_up_member]
    form = MiembroForm


admin.site.register(Miembro, MiembroAdmin)
