"""
Калькулятор повинна бути 1 ф-ція яка б приймала 3 аргументи - один з яких операція яку зробити!
"""


def calc(num1, num2, operation):
    if operation == "+":
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        return num1/num2
    else:
        return 'fiasko. Change operation'

print(calc(2, 5, '+'))
print(calc(2, 5, '-'))
print(calc(2, 5, '*'))
print(calc(2, 5, '/'))
print(calc(2, 5, ''))

if __name__ == "__main__":
    pass