# El siguiente flujo describe el proceso de una persona al despertar por
# la mañana y alistarse para salir a la calle.


# Despertar
def despertar(hora_actual=None, hora_despertar=None, *args, **kwargs):
    # Ejemplo de ejecición -> despertar() args=[] kwargs={}
    # Ejemplo de ejecición -> despertar(1) args=[1,] kwargs={0: 1}
    # Ejemplo de ejecición -> despertar(parametro=1) args=[1,] kwargs={'parametro': 1}
    # Ejemplo de ejecición -> despertar(otro_parametro=10, parametro=1) args=[10, 1,]
    #       kwargs={'parametro': 1, 'otro_parametro':10}
    #
    print("args: {key}{key}{key}{key}{key}".format(key_1=1, key=args))
    print("kwargs: {}".format(kwargs))
    if hora_actual is not None and hora_despertar is not None:
        if hora_actual == hora_despertar:
            print("Ya es hora de despertar dormilon")
        elif hora_actual > hora_despertar:
            print("Ya se te hizo tarde")
        else:
            print("sigue durmiendo")

    else:
        print("No se que hacer")


# Bañarse
def banarse(*args, **kwargs):
    # ToDO: Esta funcion requiere ser implementada
    print("Me estoy bañando")


# Desayunar
def desayunar(*args, **kwargs):
    # ToDO: Esta funcion requiere ser implementada
    print("Estoy desayunando")


# Preparar cosas
def preparar_cosas(*args, **kwargs):
    # ToDO: Esta funcion requiere ser implementada
    print("Estoy preparando mis cosas")


# Salir
def salir(*args, **kwargs):
    # ToDO: Esta funcion requiere ser implementada
    print("Ya me estoy llendo")


def main(*args, **kwargs):
    despertar()
    banarse()
    desayunar()
    preparar_cosas()
    salir()


if __name__ == "__main__":
    main()
