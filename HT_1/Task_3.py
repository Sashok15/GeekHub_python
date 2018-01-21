"""Write a script to sum of the first n positive integers."""

numbers = [1, 5, 2, 3, -5, 8, 4, -2, 4]
sum_pos_nums = 0
for num in numbers:
    if num < 0:
        break
    else:
        sum_pos_nums += num
print(sum_pos_nums)
