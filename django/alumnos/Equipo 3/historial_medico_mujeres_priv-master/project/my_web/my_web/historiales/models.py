from django.db import models
from ..mujeres.models import Mujer

class Historial(models.Model):
    clave_instituto = models.CharField(max_length=400, null=False, blank=False)
    fecha_creacion_historial = models.DateField(null=False, blank=False,auto_now_add=True)
    fecha_ultima_actualizacion = models.DateField(null=False, blank=False, auto_now_add=False)
    mujer_historial = models.ForeignKey(Mujer, on_delete=models.CASCADE)

    def __str__(self):
        return "Historial del instituto: {historial} creado el {fecha_inicio} y con ultima actualización el {fecha_ultima}".format(historial=self.clave_instituto, fecha_inicio=self.fecha_creacion_historial, fecha_ultima= self.fecha_ultima_actualizacion)

    def obtener_ultimo_diagnostico(self):
        pass

    def obtener_primer_diagnostico(self):
        pass

    def obtener_historial_completo(self):
        pass
