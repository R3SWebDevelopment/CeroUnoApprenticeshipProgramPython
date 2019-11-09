import uuid
from datetime import datetime


class MiClase:
    id = None
    nombre = None
    timestamp = None

    def __init__(self, nombre):
        self.nombre = nombre
        self.id = uuid.uuid4()
        self.timestamp = datetime.now()

    def __str__(self):
        return "{}".format(self.id)

    def __le__(self, other):
        return self.nombre.upper() < other.nombre.upper()

    def __lt__(self, other):
        return self.nombre.upper() <= other.nombre.upper()

    def __ge__(self, other):
        return self.nombre.upper() > other.nombre.upper()

    def __gt__(self, other):
        return self.nombre.upper() >= other.nombre.upper()

    def __eq__(self, other):
        return self.nombre.upper() == other.nombre.upper()

    def __ne__(self, other):
        return self.nombre.upper() != other.nombre.upper()


class Estudiante(MiClase):
    matricula = None

    def __init__(self, nombre=None, matricula="NO TIENE MATRICULA"):
        super(Estudiante, self).__init__(nombre=nombre)
        self.matricula = matricula

    def __str__(self):
        return "{} - {}".format(self.nombre, self.matricula)

    def tomar_clase(self):
        return "ESTOY TOMANDO CLASE {}".format(self.nombre)

    @classmethod
    def enrolar_estudiante(cls, persona=None, matriculas=None):
        estudiante = Estudiante()
        estudiante.matricula = matriculas
        for name, value in vars(persona).items():
            setattr(estudiante, name, value)
        return estudiante


def main():
    objeto_1 = MiClase(nombre="Ricardo")
    objeto_2 = MiClase(nombre="Edder")
    objeto_3 = MiClase(nombre="Jorge")
    lista = [
        objeto_1,
        objeto_2,
        objeto_3,
    ]
    print("Lista sin Ordenar")
    for o in lista:
        pass
        # print(o)

    print("Lista Ordenada")
    lista.sort()
    for o in lista:
        pass
        # print(o.tomar_clase())


    for name, value in vars(objeto_1).items():
        print("{} - {}".format(name, value))

    estudiante = Estudiante.enrolar_estudiante(persona=objeto_1, matriculas="A00001")
    print("Nombre estudiante: {} - Matricula: {}".format(estudiante.nombre, estudiante.matricula))


if __name__ == "__main__":
    main()
