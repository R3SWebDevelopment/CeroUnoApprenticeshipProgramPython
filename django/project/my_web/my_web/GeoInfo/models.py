from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.nombre)


class Estado(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    pais = models.ForeignKey(Pais, null=False, blank=False, related_name='estados', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(
            self.pais,
            self.nombre
        )


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    estado = models.ForeignKey(Estado, null=False, blank=False, related_name='estados', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(
            self.estado,
            self.nombre
        )
