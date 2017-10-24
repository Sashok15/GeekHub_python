"""
Написати функцію, яка буде приймати декілька значень,
одне з яких значення за замовченням(повинна бути перевірка на наявність), і у випадку якщо воно є
додати його до іншого агрументу, якщо немає - придумайте логіку що робити программі.
"""


# func suma() add two numbers. If she has one argument, then return error function call suma(2, 2) return 4

def suma(a, b=None):
    if b is not None:
        return (a+b)
    else:
        return 'fiasko. Try again'


print(suma(2, 2))

if __name__ == "__main__":
    pass
