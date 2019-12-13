from rest_framework.routers import DefaultRouter
from .views import (
    PaisViewSet,
    EstadoViewSet,
    CiudadViewSet,
)


router = DefaultRouter()
router.register(r'pais', PaisViewSet, basename='pais')
router.register(r'estado', EstadoViewSet, basename='estado')
router.register(r'ciudad', CiudadViewSet, basename='ciudad')
urlpatterns = router.urls
