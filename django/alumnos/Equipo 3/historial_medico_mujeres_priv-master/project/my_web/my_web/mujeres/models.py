from django.db import models

ENFERMEDAD_CHOICES = [
    (True, "Si"),
    (False, "No")
]

class Mujer(models.Model):
    fecha_nacimiento = models.DateField(null=False, blank=False)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=200, null=False, blank=False)
    apellido_materno = models.CharField(max_length=200, null=False, blank=False)
    direccion = models.CharField(max_length=400,null=False,blank=False)
    telefono = models.CharField(max_length=15,null=False,blank=False)
    fecha_ultima_menstruacion = models.DateField(null=False, blank=False)
    paciente_enferma = models.BooleanField(choices=ENFERMEDAD_CHOICES, default=False)

    def __str__(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombre)
