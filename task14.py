class Calculator:
    def divide(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Bo‘lishda xatolik!")

calc = Calculator()
calc.divide(10, 0)
calc.divide(10, 2)