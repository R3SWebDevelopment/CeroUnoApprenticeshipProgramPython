palindrome_words = [
    'Ababa', 'Abalaba', 'aibofobia', 'Ana', 'ala', 'arenera', 'arepera', 'anilina', 'aviva', 'Malayalam', 'Menem',
    'Neuquen', 'oro', 'Oruro', 'oso', 'ojo', 'radar', 'reconocer', 'rotor', 'salas', 'seres', 'somos', 'sometemos'
]

no_palindrome_words = [
    'hola', 'casa', 'carro', 'Automovil', 'pachuca', 'mexico',
]


def is_palindrome_word(word=None):
    if word is not None and len(word) > 1:
        # Verificar que la longitud de la palabra es par o none, si es par no utilizar pivote
        has_pivot = (len(word) % 2) == 1

        middle = int(len(word) / 2)

        # Obtener el lado izquierdo de la palabra
        left_side = word[: middle]

        # Si tiene pivote recorre el indice una posición a la derecha
        middle += 1 if has_pivot else 0

        # Obtener el lado derecha de la palabra
        right_side = word[middle:]

        # Verificar si los dos lados de la palabra son iguales
        return left_side.upper() == right_side[::-1].upper()
    return False


