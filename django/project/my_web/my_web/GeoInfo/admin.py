from django.contrib import admin

from .models import (
    Pais,
    Estado,
    Ciudad,
)


class PaisAdmin(admin.ModelAdmin):
    pass


class EstadoAdmin(admin.ModelAdmin):
    pass


class CiudadAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Ciudad, CiudadAdmin)
