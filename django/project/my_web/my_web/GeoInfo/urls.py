from django.urls import path, include

from .views import (
    country_listing
)

urlpatterns = [
    path('paises/', country_listing, name='countries'),
]
