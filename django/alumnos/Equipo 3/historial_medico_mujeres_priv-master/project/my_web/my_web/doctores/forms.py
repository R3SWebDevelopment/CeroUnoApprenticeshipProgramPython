from django import forms

from .models import Doctor

class DoctorForm(forms.ModelForm):

    class Meta:
        models = Doctor

        fields = [
            "nombre_doctor",
            "cedula_doctor",
            "direccion_doctor",
            "telefono_contacto"
        ]

        def __init__(self, *args, **kwargs):
            super(DoctorForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].required = True