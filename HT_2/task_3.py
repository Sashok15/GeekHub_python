"""
Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати якийсь результат.
Також створіть четверу ф-цію, яка в тілі викликає 3 попередні,
обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3
"""


def get_name(name):
    return 'hello ' + str(name)


def get_age(age):
    return '\nyour age is ' + str(age)


def get_pet(pet):
    return '\nyou have a pet. it is ' + str(pet)


# func return concatination three func

def call_all_function(name, age, pet):
    return get_name(name) + get_age(age) + get_pet(pet)


print(call_all_function('sashka', 20, 'dog'))
