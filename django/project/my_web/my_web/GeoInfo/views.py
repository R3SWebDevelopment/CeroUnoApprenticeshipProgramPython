from django.http import JsonResponse

from .models import (
    Pais,
    Estado,
)


def country_listing(request):
    paises = Pais.objects.all()
    data = {
        'results': [
            {
                'id': p.id,
                'text': p.nombre
            }
            for p in paises
        ],
        'count': paises.count(),
        'more': False,
    }
    return JsonResponse(data)


def state_listing(request):
    estados = Estado.objects.all()
    pais_id = request.GET.get('pais_id', None)
    if pais_id is not None:
        estados = estados.filter(pais__id=pais_id)
    data = {
        'results': [
            {
                'id': p.id,
                'text': p.nombre
            }
            for p in estados
        ],
        'count': estados.count(),
        'more': False,
    }
    return JsonResponse(data)
