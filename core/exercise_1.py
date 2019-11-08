"""
    Debe crear una funcion que reciba un parametro de tipo entero.
    Asuma que el parametro esta en el rango de 10 y 1,000,000.
    La funcion debe de regresar un valor entero que represente la sumatoria del valor representado por el
    parametro.

    Ejemplo:
    parametro = 10 -- Resultado: 50
    parametro = 1983 -- Resultado: 1967136
    parametro = 86589 -- Resultado: 3748870755
    parametro = 1 -- Resultado: Exception: The value provided is below the expect
    parametro = 394377 -- Resultado: 77766806253
"""
import sys
from utilities.runner import Runner


class Exercise(Runner):

    __mentor = False

    def __init__(self, mentor=False):
        super(Exercise, self).__init__()
        self.__mentor = mentor
        test_data = [
            {
                "parameters": {
                    "parameter_1": 10,
                },
                "expected": 55,
            },
            {
                "parameters": {
                    "parameter_1": 1983,
                },
                "expected": 1967136,
            },
            {
                "parameters": {
                    "parameter_1": 86589,
                },
                "expected": 3748870755,
            },
            {
                "parameters": {
                    "parameter_1": 394377,
                },
                "expected": 77766806253,
            },
        ]
        self.set_test_data(test_data=test_data)

    def define_callable_obj(self):
        if self.__mentor:
            from exercise_1.mentor import sumatoria
        else:
            from exercise_1.student import sumatoria
        self.set_callable_obj(callable_obj=sumatoria)


def call_tester(mentor=False):
    exercise = Exercise(mentor=mentor)
    exercise.define_callable_obj()
    exercise.run_test()
    exercise.check_test_results()
    exercise.print_results()


if __name__ == "__main__":
    mentor = True if len(sys.argv) >= 2 and sys.argv[1].upper() == "MENTOR" else False
    call_tester(mentor=mentor)
