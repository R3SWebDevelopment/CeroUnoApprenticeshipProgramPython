from django.db import models

class Doctor(models.Model):
    nombre_doctor = models.CharField(max_length=200, null=False, blank=False)
    cedula_doctor = models.CharField(max_length=200, null=False, blank=False)
    direccion_doctor = models.CharField(max_length=200, null=False, blank=False)
    telefono_contacto = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "Dr: {}".format(self.nombre_doctor)

    def crear_diagnostico(self):
        pass

    def dar_alta(self):
        pass

    def solicitar_laboratorio(self):
        pass