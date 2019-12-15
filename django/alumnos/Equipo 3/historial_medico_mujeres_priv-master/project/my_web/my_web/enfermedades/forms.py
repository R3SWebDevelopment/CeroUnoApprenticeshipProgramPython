from django import forms

from .models import Enfermedad

class EnfermedadForm(forms.ModelForm):

    class Meta:
        models = Enfermedad

        fields = [
            "clasificacion",
            "nombre_enfermedad",
            "enfermedad_mortal",
            "fecha_deteccion",
            "fecha_alta_paciente"
        ]

        def __init__(self, *args, **kwargs):
            super(EnfermedadForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].required = True