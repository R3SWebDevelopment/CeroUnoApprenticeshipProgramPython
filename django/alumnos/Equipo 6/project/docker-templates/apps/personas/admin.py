from django.contrib import admin

from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Persona, PersonaAdmin)
