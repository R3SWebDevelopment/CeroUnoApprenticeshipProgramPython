from django import forms
from django_select2.forms import ModelSelect2Widget

from .models import (
    Persona,
    Hermandad,
    GENERO_CHOICES,
    Miembro,
)
from my_web.GeoInfo.models import Pais


class PersonaForm(forms.ModelForm):

    pais = forms.ChoiceField(
        widget=ModelSelect2Widget(
            model=Pais,
            search_fields=['nombre__icontains']
        )
    )

    class Meta:
        models = Persona
        # Definimos los campos que se van a mostrar en la forma
        fields = ['nombre', 'apellido_paterno', 'genero', 'fecha_nacimiento', 'pais']

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(PersonaForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields
            if field in ['pareja', 'padre', 'madre']:
                # Si el valor de field coincide, define el campo como no requerido
                self.fields[field].required = False


class MiembroForm(PersonaForm):

    class Meta:
        models = Miembro
        # Definimos los campos que se van a mostrar en la forma
        fields = PersonaForm.Meta.fields + ['numero_membresia']


class HermandadFormSet(forms.BaseInlineFormSet):

    def get_form_kwargs(self, index):
        kwargs = super(HermandadFormSet, self).get_form_kwargs(index)
        kwargs.update({'parent': self.instance})
        return kwargs


class HermandadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200, label='Nombre')
    apellido_paterno = forms.CharField(max_length=200, label='Apellido Paterno')
    genero = forms.ChoiceField(choices=GENERO_CHOICES, label='Genero')

    class Meta:
        models = Hermandad
        # Definimos los campos que se van a mostrar en la forma
        fields = ['persona_dos', 'nombre', 'apellido_paterno', 'genero']

    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get('parent', None)
        if self.parent is not None:
            del kwargs['parent']
        # Es necesario inicializar la clase padre ModelForm
        super(HermandadForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
        if self.parent is not None:
            self.fields['persona_dos'].queryset = Persona.objects.exclude(id=self.parent.id).all()
            self.fields['persona_dos'].label = 'Seleccionar Persona'

        if self.instance is not None and len(str(self.instance).strip()) > 0:
            # La forma esta relacionada a una persona

            # Inicializar los campos nombre, apellido_paterno y genero basado en el hermano (persona) seleccionada
            self.fields['nombre'].initial = self.instance.persona_dos.nombre
            self.fields['apellido_paterno'].initial = self.instance.persona_dos.apellido_paterno
            self.fields['genero'].initial = self.instance.persona_dos.genero
        else:
            # La forma no esta relacionada a ninguna persona
            pass
