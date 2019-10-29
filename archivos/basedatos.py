ARCHIVO_DE_BASE_DE_DATOS = "database.txt"


def guardar_en_base_de_datos(datos=[], sobrescribir=False):
    sobrescribir = False if sobrescribir is None or isinstance(sobrescribir, bool) else sobrescribir
    if datos is not None and isinstance(datos, list):
        with open(ARCHIVO_DE_BASE_DE_DATOS, "a+" if not sobrescribir else "w+") as f:
            for linea in datos:
                f.write("{}\n".format(linea))


def leer_de_base_de_datos():
    datos = []
    with open(ARCHIVO_DE_BASE_DE_DATOS, "r") as f:
        for linea in f.readlines():
            datos.append(linea.strip())
    return datos


def get_personas():
    personas = []
    for registro in leer_de_base_de_datos():
        datos = registro.split(",")
        personas.append(
            {
                "nombre": datos[0] if len(datos) > 0 else None,
                "fecha_registro": datos[1] if len(datos) > 1 else None,
                "edad": datos[2] if len(datos) > 2 else None,
            }
        )
    return personas


def add_datos_personales(datos={}):
    if datos is not None and isinstance(datos, dict):
        registro = parse_data(datos)
        guardar_en_base_de_datos([registro])


def add_persona(nombre=None, fecha_registro=None, edad=None):
    add_datos_personales(
        {
            "nombre": nombre,
            "fecha_registro": fecha_registro,
            "edad": edad,
        }
    )


def filtrar_personas_por_llave(filtro=None, llave=None):
    personas = get_personas()
    if filtro is not None and filtro.strip() and llave is not None and llave.strip():
        lista_filtrada = []
        for person in personas:
            nombre = person.get(llave, None)
            if nombre is not None and nombre.strip() and filtro.upper() in nombre.upper():
                lista_filtrada.append(person)
        personas = lista_filtrada
    return personas


def filtrar_personas_por_nombre(filtro=None):
    return filtrar_personas_por_llave(filtro=filtro, llave="nombre")


def filtrar_personas_por_edad(filtro=None):
    return filtrar_personas_por_llave(filtro=filtro, llave="edad")


def filtrar_personas_por_fecha_registro(filtro=None):
    return filtrar_personas_por_llave(filtro=filtro, llave="fecha_registro")


def eliminar_personas_por_llave(filtro=None, llave=None):
    personas = get_personas()
    personas_filtradas = filtrar_personas_por_llave(filtro=filtro, llave=llave)
    personas_actualizadas = []
    for persona in personas:
        if persona not in personas_filtradas:
            personas_actualizadas.append(persona)
    actualizar_base_de_datos(datos=personas_actualizadas)


def eliminar_personas_por_nombre(filtro=None):
    return eliminar_personas_por_llave(filtro=filtro, llave="nombre")


def eliminar_personas_por_edad(filtro=None):
    return eliminar_personas_por_llave(filtro=filtro, llave="edad")


def eliminar_personas_por_fecha_registro(filtro=None):
    return eliminar_personas_por_llave(filtro=filtro, llave="fecha_registro")


def actualizar_base_de_datos(datos=[]):
    datos_actuazlizados = parse_data_list(datos)
    guardar_en_base_de_datos(datos=datos_actuazlizados, sobrescribir=True)


def parse_data_list(lista=[]):
    datos = []
    for persona in lista:
        registro = parse_data(persona)
        datos.append(registro)
    return datos


def parse_data(diccionario={}):
    nombre = diccionario.get('nombre', '')
    fecha_registro = diccionario.get('fecha_registro', '')
    edad = diccionario.get('edad', '')
    registro = "{nombre},{fecha_registro},{edad}".format(
        nombre=nombre,
        fecha_registro=fecha_registro,
        edad=edad
    )
    return registro


def actualizar_registro(persona, nuevo_nombre=None, nueva_fecha_registro=None, nueva_edad=None):
    persona_actualizada = {
        "nombre": nuevo_nombre if nuevo_nombre is not None else persona.get("nombre"),
        "fecha_registro": nueva_fecha_registro if nueva_fecha_registro is not None else persona.get("fecha_registro"),
        "edad": nueva_edad if nueva_edad is not None else persona.get("edad"),
    }
    nuevos_datos = []
    for p in get_personas():
        if p == persona:
            nuevos_datos.append(persona_actualizada)
        else:
            nuevos_datos.append(p)
    actualizar_base_de_datos(nuevos_datos)
