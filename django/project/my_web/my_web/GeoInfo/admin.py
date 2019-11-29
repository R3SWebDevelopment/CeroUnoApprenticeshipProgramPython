from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import (
    Pais,
    Estado,
    Ciudad,
)


class EstadoOnPaisTabularAdmin(admin.TabularInline):
    model = Estado
    fields = ['nombre', 'edit']
    readonly_fields = ['edit']
    extra = 0

    def edit(self, obj):
        url = reverse('admin:GeoInfo_estado_change',  args=[obj.pk])
        if obj.pk:
            return mark_safe('<a target="blank" href="{u}">edit</a>'.format(u=url))
        return ''


class PaisAdmin(admin.ModelAdmin):
    inlines = [
        EstadoOnPaisTabularAdmin,
    ]


class CiudadOnEstadoTabularAdmin(admin.TabularInline):
    model = Ciudad
    fields = ['nombre', 'edit']
    readonly_fields = ['edit']
    extra = 0

    def edit(self, obj):
        url = reverse('admin:GeoInfo_ciudad_change',  args=[obj.pk])
        if obj.pk:
            return mark_safe('<a target="blank" href="{u}">edit</a>'.format(u=url))
        return ''


class EstadoAdmin(admin.ModelAdmin):
    inlines = [
        CiudadOnEstadoTabularAdmin,
    ]


class CiudadAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Ciudad, CiudadAdmin)
