from django import forms

from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):

    class Meta:
        models = Diagnostico

        field = [
            "fecha_diagnostico",
            "recomendaciones",
            "historial_diagnostico",
            "doctor_emite_diagnostico",
        ]

        def __init__(self, *args, **kwargs):
            super(DiagnosticoForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].requiered = True
