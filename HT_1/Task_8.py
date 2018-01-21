""" Write a script to replace last value of tuples in a list.
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] """

elements = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(elements)):
    elements[i] = list(elements[i])
    elements[i][-1] = 100
    elements[i] = tuple(elements[i])
print(elements)
