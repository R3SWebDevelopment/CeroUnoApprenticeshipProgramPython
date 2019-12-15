from django.db import models
from ..diagnosticos.models import Diagnostico

class Analisis(models.Model):
    tipo_analisis = models.CharField(max_length=200, null=False, blank=False)
    fecha_de_solicitud = models.DateField(null=False, blank=False, auto_now_add=False)
    fecha_resultados = models.DateField(null=True, blank=True, auto_now_add=False)
    resultados = models.TextField(null=True, blank=True)
    analisis_del_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)

    def __str__(self):
        return "Analisis: {} con fecha: {}".format(self.tipo_analisis, self.fecha_de_solicitud)

    def obtener_resultados(self):
        pass