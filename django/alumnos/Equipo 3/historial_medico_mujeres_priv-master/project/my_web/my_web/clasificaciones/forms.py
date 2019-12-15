from django import forms

from .models import Clasificacion

class ClasificacionForm(forms.ModelForm):

    class Meta:
        models = Clasificacion

        fields = [
            "clasificacion_nombre",
            "tipo_enfermedad"
        ]

        def __init__(self, *args, **kwargs):
            super(ClasificacionForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].requiered = True