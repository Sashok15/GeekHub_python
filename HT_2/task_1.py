"""
(таких ф-цій потрібно написати 3 -> різними варіантами)
Написати функцію season, приймаючу 1 аргумент — номер місяця (від 1 до 12),
яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).
"""


# enter the number in func season(3) - it will be the month  and get season
def season(n):
    dc = {1: 'winter', 2: 'winter', 3: 'spring',
          4: 'spring', 5: 'spring', 6: 'summer',
          7: 'summer', 8: 'summer', 9: 'autumn',
          10: 'autumn', 11: 'autumn', 12: 'winter'}
    return dc.get(n, 'Eto fiasko, bratan. Try again')

print(season(16))


# enter the number in func season_1() - it will be the month  and get season
def season_1(n):
    if n == 1 or n == 2 or n == 12:
        return 'winter'
    elif n == 3 or n == 4 or n == 5:
        return 'spring'
    elif n == 6 or n == 7 or n == 8:
        return 'summer'
    elif n == 9 or n == 10 or n == 11:
        return 'autumn'
    else:
        return 'Eto fiasko, bratan. Try again'

print(season_1(12))


# enter the number in func season_2() - it will be the month  and get season
def season_2(n):
    if n in [1, 2, 12]:
        return 'winter'
    elif n in [3, 4, 5]:
        return 'spring'
    elif n in [6, 7, 8]:
        return 'summer'
    elif n in [9, 10, 11]:
        return 'autumn'
    else:
        return 'Eto fiasko, bratan. Try again'

print(season_2(6))