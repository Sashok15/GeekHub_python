"""Створіть 3 класи, 2 з яких будуть успадковуватись один від одного!
В суперкласі мається метод __init__ який приймає 2 атребути.
Перегрузіть конструктор класу в дочірньому класі так, щоб додався ще один атребут.

"""


class A(object):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2


class B(A):
    def __init__(self, b1, b2):
        A.__init__(self, a1='a1b', a2='a2b')
        self.b1 = b1
        self.b2 = b2


class C(B):
    def __init__(self, c1, c2):
        B.__init__(self, b1='b1c', b2='b2c')
        self.c1 = c1
        self.c2 = c2


a = A('a1', 'a2')
b = B('b1', 'b2')
print(b.a1)  # a1b

c = C('c1', 'c2')
print(c.a1)  # a1b
print(c.b1)  # b1c
