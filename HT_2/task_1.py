"""
(таких ф-цій потрібно написати 3 -> різними варіантами)
Написати функцію season, приймаючу 1 аргумент — номер місяця (від 1 до 12),
яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""


# enter the number in func season(3) - it will be the month  and get season
def season(num_month):
    dc = {1: 'winter', 2: 'winter', 3: 'spring',
          4: 'spring', 5: 'spring', 6: 'summer',
          7: 'summer', 8: 'summer', 9: 'autumn',
          10: 'autumn', 11: 'autumn', 12: 'winter'}
    return dc.get(num_month, 'No such number month. Try again')


print(season(16))


# enter the number in func season_1() - it will be the month  and get season
def season_1(num_month):
    if num_month == 1 or num_month == 2 or num_month == 12:
        return 'winter'
    elif num_month == 3 or num_month == 4 or num_month == 5:
        return 'spring'
    elif num_month == 6 or num_month == 7 or num_month == 8:
        return 'summer'
    elif num_month == 9 or num_month == 10 or num_month == 11:
        return 'autumn'
    else:
        return 'No such number month. Try again'


print(season_1(12))


# enter the number in func season_2() - it will be the month  and get season
def season_2(num_moth):
    if num_moth in [1, 2, 12]:
        return 'winter'
    elif num_moth in [3, 4, 5]:
        return 'spring'
    elif num_moth in [6, 7, 8]:
        return 'summer'
    elif num_moth in [9, 10, 11]:
        return 'autumn'
    else:
        return 'No such number month. Try again'


print(season_2(6))
