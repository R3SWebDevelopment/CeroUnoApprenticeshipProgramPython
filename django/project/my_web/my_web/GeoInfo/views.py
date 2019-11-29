from django.http import JsonResponse

from .models import (
    Pais,
    Estado,
    Ciudad,
)


def country_listing(request):
    paises = Pais.objects.all()
    q = request.GET.get('q', None)
    if q is not None:
        paises = paises.filter(nombre__icontains=q)
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
    q = request.GET.get('q', None)
    if q is not None:
        estados = estados.filter(nombre__icontains=q)
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


def city_listing(request):
    ciudades = Ciudad.objects.all()
    estado_id = request.GET.get('estado_id', None)
    if estado_id is not None:
        ciudades = ciudades.filter(estado__id=estado_id)
    q = request.GET.get('q', None)
    if q is not None:
        ciudades = ciudades.filter(nombre__icontains=q)
    data = {
        'results': [
            {
                'id': p.id,
                'text': p.nombre
            }
            for p in ciudades
        ],
        'count': ciudades.count(),
        'more': False,
    }
    return JsonResponse(data)
