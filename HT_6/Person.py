"""Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
які зберігатиме в відповідні змінні. Методи, які повинні бути в класі
Person - show_age, print_name, show_all_information.

Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.

"""


class Person(object):
    def __init__(self, *args):
        self.args = args

    # work with first argument
    def show_age(self):
        return self.args[0]

    # work with second argument
    def print_name(self):
        return self.args[1]

    def show_all_information(self):
        return self.args


person_1 = Person(36, "Sashka", "freelancer")
person_2 = Person(25, "Olya", "accountant")  # accountant - бухгалтер

print(person_1.show_age())  # 36
print(person_1.show_all_information())  # (36, 'Sashka', 'freelancer')

