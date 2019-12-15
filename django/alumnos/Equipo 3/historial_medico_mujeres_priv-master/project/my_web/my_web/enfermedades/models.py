from django.db import models

class Enfermedad(models.Model):
    clasificacion = models.CharField(max_length=200, null=False, blank=False)
    nombre_enfermedad = models.CharField(max_length=200, null=False, blank=False)
    enfermedad_mortal = models.BooleanField(default=False)
    fecha_deteccion = models.DateField(null=False, blank=False, auto_now_add=False)
    fecha_alta_paciente = models.DateField(null=False, blank=False, auto_now_add=False)

    def __str__(self):
        return "Enfermedad: {nombre_enf} detectada el {fecha_detectada}".format(nombre_enf=self.nombre_enfermedad, fecha_detectada=self.fecha_deteccion)

    def calcular_tiempo_enfermedad(self):
        pass

    def dar_alta(self):
        pass
