from bs4 import BeautifulSoup
import requests
from my_web.GeoInfo.models import (
    Estado,
    Ciudad,
)


def fetch_hidalgo():
    hidalgo = Estado.objects.filter(nombre__icontains='hidalgo').first()

    if hidalgo is not None:
        url = 'https://es.wikipedia.org/wiki/Anexo:Municipios_del_estado_de_Hidalgo'
        response = requests.get(url)
        if response.ok:
            html = response.content
            soup = BeautifulSoup(html)
            tablas = soup.findAll('table')
            if len(tablas) > 0:
                tabla = tablas[0]
                lineas = tabla.findAll('tr')
                for linea in lineas:
                    columnas = linea.findAll('td')
                    if len(columnas) > 2:
                        nombre = columnas[1].text.strip()
                        instance, created = Ciudad.objects.get_or_create(nombre=nombre, estado=hidalgo)
                        print("Ciudad: {} fue Creada: {} - {}".format(
                            nombre,
                            created,
                            instance
                        ))
        else:
            print("Algo salio mal")
    else:
        print("El estado no existe")
