from django.db import models

class Clasificacion(models.Model):
    clasificacion_nombre = models.CharField(null=False, blank=False, max_length=200)
    tipo_enfermedad = models.CharField(null=False, blank=False, max_length=200)

    def __str__(self):
        return "{}".format(self.clasificacion_nombre)