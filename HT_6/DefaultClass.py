"""Створіть клас, який називається DefaultClass що має атрибути об'єкту name, symbol number .
Виведіть атребути.

Створіть словник з наступними ключами і значеннями: 'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20 .
Далі створіть об'єкт з ім'ям user класу DefaultClass1 за допомогою цього словника.

Для класу DefaultClass1 визначте метод з ім'ям print_info() ,
що виводить на екран значення атрибутів об'єкта (name , l_name та age ).

"""


class DefaultClass(object):
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


dc = DefaultClass("Class", "C", 23)
print(dc.name, dc.symbol, dc.number)  # Class C 23


class DefaultClass1(object):
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def get_info(self):
        list_values = []
        for key, value in self.my_dict.items():
            list_values.append(value)
        return list_values


dict_ = {'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20}
user = DefaultClass1(dict_)
print(user.get_info())  # ['Vasya', 'Pupkin', 20]
