import re
REG_EXP_NUMBER = r"[0-9]*(\.[0-9]*)?"
REG_EXP_SIMPLE_OPERATION = r"[0-9]*(\.[0-9]*)?\s[\+\-]?\s[0-9]*(\.[0-9]*)?"
REG_EXP_SIMPLE_OPERATION_PARENTESIS = r"\([0-9]*(\.[0-9]*)?\s[\+\-]?\s[0-9]*(\.[0-9]*)?\)"


def _operacion_aritmetica(operacion=None, signo=None):
    """
    Función que realiza suma de dos operandos
    :param operacion: Cadena con una operacion aritmetica basica dos operadores
    :param signo: Signo de operacion aritmetica
    :return: Regresa un entero con el resultado, regresa None si no puede realizar la operacion aritmetica
    """
    resultado = None
    if operacion and signo in ['-', '+']:
        operadores = operacion.split(signo)
        for operador in operadores:
            try:
                valor = float(operador)
            except Exception as e:
                return None
            if resultado is None:
                resultado = valor
            elif signo == '-':
                resultado -= valor
            else:
                resultado += valor
    return resultado


def suma(operacion=None):
    """
    Función que realiza suma de dos operandos
    :param operacion: Cadena con una operacion aritmetica basica (Suma) dos operadores
    :return: Regresa un entero con el resultado, regresa None si no puede realizar la operacion aritmetica
    """
    return _operacion_aritmetica(operacion=operacion, signo='+')


def resta(operacion=None):
    """
    Función que realiza resta de dos operandos
    :param operacion: Cadena con una operacion aritmetica basica (Resta) dos operadores
    :return: Regresa un entero con el resultado, regresa None si no puede realizar la operacion aritmetica
    """
    return _operacion_aritmetica(operacion=operacion, signo='-')


def operaciones_aritmeticas_multiples(operacion=None):
    """
    Funcion que realiza operacion aritmetica con multiples operadores y signos
    :param operacion: Cadena con una operacion aritmetica de multiples operadores y signos
    :return: Regresa un entero con el resultado, regresa None si no puede realizar la operacion aritmetica
    """
    # print("operacion: {}".format(operacion))
    def _simplify_operations(left_operator=None, right_operator=None):
        if left_operator is not None and right_operator is not None:
            if '-' in left_operator or '+' in left_operator:
                # Si encuentra un isgno de suma o resta significa que adentro de la cadena todavia hay una operacion
                # aritmetica
                left_operator = operaciones_aritmeticas_multiples(left_operator)
            if '-' in right_operator or '+' in right_operator:
                # Si encuentra un isgno de suma o resta significa que adentro de la cadena todavia hay una operacion
                # aritmetica
                right_operator = operaciones_aritmeticas_multiples(right_operator)
        return left_operator, right_operator
    resultado = None
    # Tratar de simplificar una operacion
    if operacion is not None:
        index_signo = operacion.find('+')
        if index_signo != -1:
            left_operator = operacion[: index_signo]
            right_operator = operacion[index_signo + 1:]
            left_operator, right_operator = _simplify_operations(
                left_operator=left_operator, right_operator=right_operator
            )
            if left_operator is not None and right_operator is not None:
                resultado = suma("{} + {}".format(left_operator, right_operator))
        else:
            index_signo = operacion.find('-')
            if index_signo != -1:
                left_operator = operacion[: index_signo]
                right_operator = operacion[index_signo + 1:]
                left_operator, right_operator = _simplify_operations(
                    left_operator=left_operator, right_operator=right_operator
                )
                if left_operator is not None and right_operator is not None:
                    resultado = resta("{} - {}".format(left_operator, right_operator))
    return resultado


def operacione_complejas(operacion=None):
    resultado = None
    if operacion:
        keep_normalizing = operacion.find('(') != -1 and operacion.find(')') != -1
        while keep_normalizing:
            operacion = normalizar_operacione_complejas(operacion=operacion)
            keep_normalizing = operacion.find('(') != -1 and operacion.find(')') != -1
        resultado = operaciones_aritmeticas_multiples(operacion=operacion)
    return resultado


def normalizar_operacione_complejas(operacion=None):
    matches = re.finditer(REG_EXP_SIMPLE_OPERATION_PARENTESIS, operacion, re.MULTILINE)
    mapped_operacion = []
    for matchNum, match in enumerate(matches, start=1):
        sub_operation = match.group().replace("(", "").replace(")", "")
        sub_operation_resultado = operaciones_aritmeticas_multiples(sub_operation)
        mapped_operacion.append(
            {
                "operation": sub_operation,
                "start": match.start(),
                "end": match.end(),
                'result': sub_operation_resultado,
            }
        )
    for sub_operation in mapped_operacion[::-1]:
        start = sub_operation.get('start', 0)
        end = sub_operation.get('end', 0)
        result = sub_operation.get('result', 0)
        operacion = "{}{}{}".format(
            operacion[:start],
            str(result),
            operacion[end:]
        )

    return operacion
