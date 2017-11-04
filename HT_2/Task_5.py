"""
маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
створюєте ф-цію яка буде отримувати рядки на зразок мого, яка працює в 4 випадках:
    якщо довжина рядка в діапазоні 30-50 -> прінтує довжину, кількість букв та цифр
    якщо довжина менше 30 -> прінтує суму всіх чисел та окремо рядок без цифр лише з буквами
    якщо довжина бульше 50 - > ваша фантазія
    звісно 4 все інше
"""
import re
s_1 = "f98neroi4nr0c3n30irn03ien3c0rfeasd"
s_2 = 'f98neroi4nr0c3n30i'
s_3 = "kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"


def func(s_arg):
    if 30 <= len(s_arg) <= 50:
        count_char = re.findall(r'\D', s_arg)
        count_numbers = re.findall(r'\d+', s_arg)
        return "Довжина рядка - {0}\nКількість букв - {1}\nКількість цифр - {2}\n".format\
            ( len(s_arg), len(count_char), len(count_numbers))
    elif len(s_arg) < 30:
        numbers = re.findall(r'\d+', s_arg)
        count_char = re.findall(r'\D', s_arg)
        numbers_sum = 0
        for n in numbers:
            numbers_sum += int(n)
        return "Сума всіх чисел - {0}\nЛише букви - {1}\n".format(numbers_sum, count_char)
    else:
        return "string big, cut his, plese"


print(func(s_1))
print(func(s_2))
print(func(s_3))