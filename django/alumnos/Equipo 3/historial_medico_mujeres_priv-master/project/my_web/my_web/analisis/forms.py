from django import forms

from .models import Analisis

class AnalisisForm(forms.ModelForm):

    class Meta:
        models = Analisis

        fields = [
            'tipo_analisis',
            'fecha_de_solicitud',
            'fecha_resultados',
            'resultados',
            'analisis_del_diagnostico'
        ]

        def __init__(self, *args, **kwargs):
            super(AnalisisForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].required = True