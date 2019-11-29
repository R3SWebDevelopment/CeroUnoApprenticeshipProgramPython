from django.urls import path, include

from .views import (
    country_listing,
    state_listing,
    city_listing,
)

urlpatterns = [
    path('paises/', country_listing, name='countries'),
    path('paises/estado/', state_listing, name='states'),
    path('paises/estado/ciudad/', city_listing, name='cities'),
]
