from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import filters

from .serializers import (
    PaisSerializer,
    EstadoSerializer,
    CiudadSerializer,
)


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


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['nombre', ]


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['nombre', 'pais__nombre']


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['nombre', 'estado__nombre', 'estado__pais__nombre']
