"""Напишіть програму в стилі ООП, що задовольняє наступним умовам:
у програмі повинні бути два класи та два об'єкта, що належать різним класам;
один об'єкт за допомогою методу свого класу повинен так чи інакше змінювати дані іншого об'єкта

Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

"""


class Human(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count += 1

    @staticmethod
    def fill_cup():
        Cup.capacity += 5

    @staticmethod
    def count_instance():
        return Human.count


class Cup(object):
    capacity = 0

h1 = Human('dima', 20)
print(Human.count_instance())  # 1 instance

h2 = Human('max', 30)
print(Human.count_instance())  # 2 instance

print(Cup.capacity)  # 0

h1.fill_cup()
print(Cup.capacity)  # 5
