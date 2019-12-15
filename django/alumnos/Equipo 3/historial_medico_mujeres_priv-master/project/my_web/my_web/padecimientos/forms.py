from django import forms

from .models import Padecimiento

class PadecimientoForm(forms.ModelForm):

    class Meta:
        models = Padecimiento

        fields = [
            "nombre_padecimiento",
            "descripcion_padecimiento",
            "intensidad_padecimiento"
        ]

        def __init__(self, *args, **kwargs):
            super(PadecimientoForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].requiered = True