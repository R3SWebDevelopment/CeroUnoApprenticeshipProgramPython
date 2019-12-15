from django import forms

from .models import Historial

class HistorialForm(forms.ModelForm):

    class Meta:
        models = Historial

        fields = [
            'clave_instituto',
            'fecha_ultima_actualizacion',
            'mujer_historial'
        ]

        def __init__(self, *args, **kwargs):
            super(HistorialForm, self).__init__(*args,**kwargs)
            for field in self.fields:
                self.fields[field].required = True