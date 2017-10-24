"""
Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати якийсь результат.
Також створіть четверу ф-цію, яка в тілі викликає 3 попередні,
обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3
"""


def which_name(name):
    return 'hello ' + str(name)


def which_age(age):
    return '\nyour age is ' + str(age)


def which_pet(pet):
    return '\nyou have a pet. it is ' + str(pet)


# func return concatination three func: which_name, which_age, which+pet
# exaple call print(call_all_function('sashka', 20, 'dog'))
def call_all_function(name, age, pet):
    return which_name(name)+which_age(age)+which_pet(pet)

print(call_all_function('sashka', 20, 'dog'))

if __name__ == "__main__":
    pass