""" Write a script to replace last value of tuples in a list.
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] """

li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(li)):
    li[i] = list(li[i])
    li[i][-1] = 100
    li[i] = tuple(li[i])
print(li)