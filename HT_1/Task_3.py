"""Write a script to sum of the first n positive integers."""

a = [1, 5, 2, 3, -5, 8, 4, -2, 4]
k = 0
for i in a:
    if i < 0:
        break
    else:
        k += i
print(k)