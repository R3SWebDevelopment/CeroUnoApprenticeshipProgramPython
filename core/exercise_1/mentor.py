def sumatoria(parameter_1=0, gauss=True):
    if parameter_1 < 10:
        raise Exception("The value provided is below the expect")
    if gauss:
        return (parameter_1 * (parameter_1 + 1)) / 2
    else:
        total = 0
        for x in range(parameter_1 + 1):
            total += x
        return total
