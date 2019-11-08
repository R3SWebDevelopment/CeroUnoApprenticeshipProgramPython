class Runner:

    __callable_obj = None
    __test_data = None

    def set_callable_obj(self, callable_obj=None):
        if not callable(callable_obj):
            raise Exception("The callable object pass is not a callable object")
        self.__callable_obj = callable_obj

    def get_callable_obj(self):
        if self.__callable_obj is None:
            raise Exception("Callable Object has not been defined")
        return self.__callable_obj

    def set_test_data(self, test_data=[]):
        self.__test_data = test_data

    def get_test_data(self):
        if self.__test_data is None or not isinstance(self.__test_data, list) or len(self.__test_data) == 0:
            raise Exception("The test data has not been defined")
        return self.__test_data

    def run_test(self):
        test_data = self.get_test_data()
        callable_obj = self.get_callable_obj()
        for test in test_data:
            if isinstance(test, dict):
                parameters = test.get("parameters", None)
                if parameters is None:
                    test.update(
                        {
                            "result": "Not Executed"
                        }
                    )
                else:
                    try:
                        result = callable_obj(**parameters)
                        test.update(
                            {
                                "result": result
                            }
                        )
                    except Exception as e:
                        test.update(
                            {
                                "result": str(e)
                            }
                        )

    def check_test_results(self):
        test_data = self.get_test_data()
        for test in test_data:
            expected = test.get('expected', None)
            result = test.get('result', None)
            if expected == result:
                test.update(
                    {
                        "test_ok": True
                    }
                )
            else:
                test.update(
                    {
                        "test_ok": False
                    }
                )

    def print_results(self):
        test_data = self.get_test_data()
        print("Entrada                      | Salida Esperada               | Salida Recibida           | OK")
        for test in test_data:
            salida = "{in}                      | {expected}               | {out}           | {ok}".format(
                **{
                    "in": test.get('parameters', ""),
                    "expected": test.get('expected', ""),
                    "out": test.get('result', ""),
                    "ok": test.get('test_ok', ""),
                }
            )
            print(salida)
