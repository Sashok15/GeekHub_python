"""
Створіть 2 змінні x та y з довільними значеннями;
Створіть просту умовну конструкцію(звісно вона повинна бути в тілі ф-ції),
під час виконання якої буде перевірятися рівність змінних x та y.
Удоскональте конструкцію та додайте відповідні умови,
які б при нерівності змінних х та у відповідь повертали різницю чисел.
Повинні опрацювати такі умови:
    x > y; відповідь - х більше ніж у на z
    x < y; відповідь - у більше ніж х на z
    x==y. відповідь - х дорівнює z
"""
x, y = int(input()), int(input())


# func(x, y) call so, where x = number and y = number
def func(x, y):
    if x == y:
        z = x
        return z
    elif x > y:
        z = x - y
        return z
    elif x < y:
        z = y-x
        return z


print(func(x, y))

if __name__ == "__main__":
    pass