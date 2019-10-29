from random import choice


def generate_choices(base=0, roof=10):
    """
    Funcion que genera un lista de opciones para el experimento
    :param base: Entero base para la generación de numeros
    :param roof: Entero tope para la generación de numeros
    :return: Lista de cadenas represetando numeros enteros
    """
    choices = [str(item) for item in range(base, roof)]
    return choices


def generate_experiment_data(universe=[], times=100000):
    """
    Funcion que simula la ejecución de un experimento n numero de veces
    :param universe: Lista de caracteres que representa las opciones del experimento
    :param times: Entero que representa el numero de veces a repetir el experimento
    :return: Listado de caracteres tomados del universo
    """
    data = []
    for _ in range(times):
        data.append(choice(universe))
    return data


def report_experiment(data=[]):
    keys = set(data)

    # Inicializar diccionario de reportes
    report = {
        str(key): 0 for key in keys
    }

    # Ordenar datos
    data.sort()

    for item in data:
        report.update(
            {
                str(item): report.get(item, 0) + 1
            }
        )

    # imprimir los resultados ordenados por numero de apariciones
    for key, times in sorted(report.items(), key=lambda x: x[1], reverse=True):
        print("opcion: {} - apariciones: {}".format(key, times))
