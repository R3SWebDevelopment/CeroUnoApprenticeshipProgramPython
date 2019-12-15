from django.db import models

class Padecimiento(models.Model):
    nombre_padecimiento = models.CharField(max_length=200, null=False, blank=False)
    descripcion_padecimiento = models.TextField(null=False, blank=False, max_length=300)
    intensidad_padecimiento = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "Padecimiento: {nombre}".format(nombre = self.nombre_padecimiento)
