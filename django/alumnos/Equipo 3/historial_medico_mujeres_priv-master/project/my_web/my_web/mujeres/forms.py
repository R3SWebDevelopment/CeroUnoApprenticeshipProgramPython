from django import forms

from .models import (
    Mujer,
    ENFERMEDAD_CHOICES
)

class MujerForm(forms.ModelForm):

    class Meta:
        model = Mujer

        fields = ['nombre','fecha_nacimiento','apellido_paterno','apellido_materno','direccion','telefono','paciente_enferma','fecha_ultima_menstruacion']

        def __init__(self, *args, **kwargs):
            super(MujerForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].required = True