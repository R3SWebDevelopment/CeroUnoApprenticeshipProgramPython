from django.urls import path, include

from .views import (
    persona_listing,
    persona_detail,
    member_listing,
    member_detail,
)

urlpatterns = [
    path('personas/', persona_listing, name='personas'),
    path('personas/<int:persona_id>/', persona_detail, name='persona'),
    path('miembros/', member_listing, name='miembros'),
    path('miembros/<int:member_id>/', member_detail, name='miembro'),
]