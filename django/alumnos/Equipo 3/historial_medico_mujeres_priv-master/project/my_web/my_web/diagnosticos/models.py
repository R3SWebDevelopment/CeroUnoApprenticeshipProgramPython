from django.db import models
from ..historiales.models import Historial
from ..doctores.models import Doctor

class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    fecha_diagnostico = models.DateField(null=False, blank=False, auto_now_add=True)
    recomendaciones = models.TextField(null=False, blank=False, max_length=900)
    historial_diagnostico = models.ForeignKey(Historial, on_delete=models.CASCADE, blank=True)
    doctor_emite_diagnostico = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "Historial: #{} creado el {} ".format(self.id_diagnostico, self.fecha_diagnostico)

