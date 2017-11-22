"""Створити клас Calc, який буде мати атребут last_result та 4 методи.

Методи повинні виконувати математичні операції з 2-ма числами, а
 саме додавання, віднімання, множення, ділення.

 Якщо під час створення екземпляру класу звернутися до атребута last_result
 він повинен повернути пусте значення

Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.

Додати документування в клас

 """


class Calc(object):
    """ This class have four methods:

    mult_num - makes multiplication of two numbers
    add_num - makes add of two numbers
    sub_num - makes substraction of two numbers
    div_num - makes division of two numbers

    """
    last_result = None

    def mult_num(self, x, y):
        last_result = x * y
        return last_result

    def add_num(self, x, y):
        last_result = x + y
        return last_result

    def sub_num(self, x, y):
        last_result = x - y
        return last_result

    def div_num(self, x, y):
        last_result = x / y
        return last_result


my_calc = Calc()
print(my_calc.last_result)  # None
print(my_calc.mult_num(6, 3))  # 18
print(my_calc.add_num(6, 3))  # 9
print(my_calc.sub_num(6, 3))  # 3
print(my_calc.div_num(6, 3))  # 2.0

