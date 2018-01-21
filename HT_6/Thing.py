"""Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу.
Виведіть типи зазначених об'єктів.

Створіть новий клас Thing2 і призначте йому атрибут letters зі значенням 'abc' .
Виведіть на екран значення атрибута letters.

Створіть ще один клас Thing3 .
Присвойте значення 'xyz' атрибуту об'єкта, який називається letters.
Виведіть на екран значення атрибута letters .

"""


class Thing(object):
    pass


print(type(Thing))  # <class 'type'>

t = Thing
print(type(t))  # <class 'type'>

t = Thing()
print(type(t))  # <class '__main__.Thing'>


class Thing2(object):
    letters = "abs"


print(Thing2.letters)


class Thing3(object):
    def __init__(self, letters):
        self.letters = letters


t3 = Thing3("xyz")
print(t3.letters)
