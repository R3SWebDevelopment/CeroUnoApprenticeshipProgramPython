from django.urls import path
from .views import index, pag1
from .views import index, pag2
from .views import index, pag3
from .views import index, pag4
from .views import index, pag5
from .views import index, pag6
from .views import index, pag7
from .views import index, pag8
from .views import index, pag9
from .views import index, pag10
from .views import index, pag11
from .views import index, pag12
from .views import index, pag13
from .views import index, pag14
from .views import index, pag15
from .views import index, pag16
from .views import index, pag17
from .views import index, pag18
from .views import index, pag19
from .views import index, pag20
from .views import index, pag21
from .views import index, pag22
from .views import index, UNIDAD1
from .views import index, UNIDAD2
from .views import index, UNIDAD3
from .views import index, UNIDAD4
from .views import index, UNIDAD5
from .views import index, UNIDAD6
from .views import index, UNIDAD7

urlpatterns = [
    path('' ,index, name="inicio"),
    path('pag1/', pag1, name='pag_uno'),
    path('pag2/', pag2, name='pag_dos'),
    path('pag3/', pag3, name='pag_tres'),
    path('pag4/', pag4, name='pag_cuatro'),
    path('pag5/', pag5, name='pag_cinco'),
    path('pag6/', pag6, name='pag_seis'),
    path('pag7/', pag7, name='pag_siete'),
    path('pag8/', pag8, name='pag_ocho'),
    path('pag9/', pag9, name='pag_nueve'),
    path('pag10/', pag10, name='pag_diez'),
    path('pag11/', pag11, name='pag_once'),
    path('pag12/', pag12, name='pag_doce'),
    path('pag13/', pag13, name='pag_trece'),
    path('pag14/', pag14, name='pag_catorce'),
    path('pag15/', pag15, name='pag_quince'),
    path('pag16/', pag16, name='pag_dieciseis'),
    path('pag17/', pag17, name='pag_diecisiete'),
    path('pag18/', pag18, name='pag_dieciocho'),
    path('pag19/', pag19, name='pag_diecinueve'),
    path('pag20/', pag20, name='pag_veinte'),
    path('pag21/', pag21, name='pag_veintiuno'),
    path('pag22/', pag22, name='pag_veintidos'),
    path('UNIDAD1/', UNIDAD1, name='UNIDAD1'),
    path('UNIDAD2/', UNIDAD2, name='UNIDAD2'),
    path('UNIDAD3/', UNIDAD3, name='UNIDAD3'),
    path('UNIDAD4/', UNIDAD4, name='UNIDAD4'),
    path('UNIDAD5/', UNIDAD5, name='UNIDAD5'),
    path('UNIDAD6/', UNIDAD6, name='UNIDAD6')
]
