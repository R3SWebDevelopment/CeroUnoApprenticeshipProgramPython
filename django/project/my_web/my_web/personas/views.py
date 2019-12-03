from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
import json


from .models import (
    Persona,
    Miembro,
)
from .forms import (
    PersonaForm,
    MiembroForm,
)


def example_display(request):
    context = {
        "result_url": reverse('example_view')
    }
    template = loader.get_template('example.html')
    return HttpResponse(template.render(context, request))


def example_view(request):

    # Aqui recibimos los valores de la matrix
    matrix = request.GET.get('matrix', None)

    if matrix is not None:
        matrix = json.loads(matrix)

    print("matrix: {}".format(matrix))


    # Aqui mandamos una matrix de 5 x 1
    data = {
        "matrix_data": [
            [7],
            [2],
            [4],
            [10],
            [3],
        ],
        "matrix_size": [5, 1]
    }

    return JsonResponse(data)


def persona_listing(request):
    personas = Persona.objects.all()

    lista = []
    for index, persona in enumerate(personas):
        lista.append(
            {
                0: str(index + 1),
                1: persona.nombre_completo,
                2: persona.genero_label,
                3: persona.genero_label,
                4: persona.is_member,
                'link': {
                    'url': reverse('persona', kwargs={
                        'persona_id': persona.id
                    }),
                    'label': 'Detalle'
                },
            }
        )

    lista_data = {
        'lista': lista,
        'columnas': [
            'No.', 'Nombre', 'Genero', 'Nacionalidad', 'Es Miembro', 'Detalle'
        ]
    }

    context = {
        'lista': lista_data,
    }
    template = loader.get_template('personas/persona_listing.html')
    return HttpResponse(template.render(context, request))


def persona_detail(request, persona_id=None):
    if persona_id is not None:
        persona = get_object_or_404(Persona, pk=persona_id)
        if request.method == 'POST':
            form = PersonaForm(request.POST, instance=persona)
        else:
            form = PersonaForm(instance=persona)
        context = {
            'form': form,
            'pais_url': reverse('countries'),
            'estado_url': reverse('states'),
            'ciudad_url': reverse('cities'),
        }
        template = loader.get_template('personas/persona_detail.html')
        return HttpResponse(template.render(context, request))
    raise Http404("No existe la persona seleccionada")


def member_listing(request):
    miembros = Miembro.objects.all()

    lista = []
    for index, persona in enumerate(miembros):
        lista.append(
            {
                0: str(index + 1),
                1: persona.nombre_completo,
                2: persona.genero_label,
                3: persona.genero_label,
                4: persona.numero_membresia,
                'link': {
                    'url': reverse('miembros'),
                    'label': 'Detalle'
                },  #persona.id
            }
        )

    lista_data = {
        'lista': lista,
        'columnas': [
            'No.', 'Nombre', 'Genero', 'Nacionalidad', 'Numero Miembro', 'Detalle'
        ]
    }

    context = {
        'lista': lista_data,
    }
    template = loader.get_template('personas/member_listing.html')
    return HttpResponse(template.render(context, request))


def member_detail(request, member_id=None):
    pass
