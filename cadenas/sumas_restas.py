"""
Basica
    1 + .0 --> 1.0
    10 - 9 --> 1
    1920 + 80 --> 2000
    9823 - .5 --> 9822.5
"""
operacion_1 = '1 + .0'
operacion_2 = '10 - 9'
operacion_3 = '1920 + 80'
operacion_4 = '9823 - .5'
"""
Multiple
    1 + 9 - 1 + 90 --> 99
    10 - 10 + 90 + 10 --> 100
    1920 + 80 - 40 - 30 --> 1930
    .5 - .5 + 3 + 9 - 10 --> 1
"""
operacion_5 = '1 + 9 - 1 + 90'
operacion_6 = '10 - 10 + 90 + 10'
operacion_7 = '1920 + 80 - 40 - 30'
operacion_8 = '.5 - .5 + 3 + 9 - 10'
"""
Parentesis 
    (1 + (9 - 1)) + 90 --> 99
    (10 - 10) + (90 + 10) --> 100
    1920 + (80 - (40 - 30)) --> 1990
    .5 - (.5 + 3) + (9 - 10) --> -4
"""
operacion_9 = '(1 + (9 - 1)) + 90'
operacion_10 = '(10 - 10) + (90 + 10)'
operacion_11 = '1920 + (80 - (40 - 30))'
operacion_12 = '.5 - (.5 + 3) + (9 - 10)'

from cadenas.aritmetica import (
    suma,
    resta,
    operaciones_aritmeticas_multiples,
    operacione_complejas,
)


def operaciones_basicas():
    print(operacion_1)
    print(suma(operacion_1))
    print(operacion_2)
    print(resta(operacion_2))
    print(operacion_3)
    print(suma(operacion_3))
    print(operacion_4)
    print(resta(operacion_4))


def operaciones_multiples():
    print(operacion_5)
    print(operaciones_aritmeticas_multiples(operacion_5))
    print(operacion_6)
    print(operaciones_aritmeticas_multiples(operacion_6))
    print(operacion_7)
    print(operaciones_aritmeticas_multiples(operacion_7))
    print(operacion_8)
    print(operaciones_aritmeticas_multiples(operacion_8))


def operaciones_parentesis():
    print(operacion_9)
    print(operacione_complejas(operacion=operacion_9))
    print(operacion_10)
    print(operacione_complejas(operacion=operacion_10))
    print(operacion_11)
    print(operacione_complejas(operacion=operacion_11))
    print(operacion_12)
    print(operacione_complejas(operacion=operacion_12))
