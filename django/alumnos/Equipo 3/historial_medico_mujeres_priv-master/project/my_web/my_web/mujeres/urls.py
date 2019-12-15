from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.print_mujeres, name="listar_mujeres"),
    path("prueba_ruben/", views.print_ruben_test, name="tst_ruben")
]