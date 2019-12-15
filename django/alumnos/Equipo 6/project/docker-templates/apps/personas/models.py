from django.db import models

GENERO_CHOICES = [
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
]


class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=200, null=False, blank=False)
    fecha_nacimiento = models.DateTimeField(null=False, blank=False)
    genero = models.CharField(max_length=1, null=False, blank=False, choices=GENERO_CHOICES)
    padre = models.ForeignKey('Persona', null=False, blank=False, related_name='hijos_del_padre')
    madre = models.ForeignKey('Persona', null=False, blank=False, related_name='hijos_de_la_madre')
    hermanos = models.ManyToManyField('Persona')
    pareja = models.OneToOneField('Persona', null=True, blank=False)
