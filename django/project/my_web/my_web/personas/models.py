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
    padre = models.ForeignKey('Persona', null=True, blank=False, related_name='hijos_del_padre', on_delete=models.CASCADE)
    madre = models.ForeignKey('Persona', null=True, blank=False, related_name='hijos_de_la_madre', on_delete=models.CASCADE)
    hermanos = models.ManyToManyField('Persona', related_name='mis_hermanos')
    pareja = models.OneToOneField('Persona', null=True, blank=False, on_delete=models.CASCADE, related_name='mi_pareja')

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido_paterno)
