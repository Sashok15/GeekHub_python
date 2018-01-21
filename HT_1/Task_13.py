"""Write a script to get the maximum and minimum value in a dictionary."""

dictionary = {1: 7, 2: 0, 3: 7, 4: -24, 5: -3, 6: -10}
max_value = dictionary[1]
min_value = dictionary[1]
for key, value in dictionary.items():
    if value >= max_value:
        max_value = value
    elif value < min_value:
        min_value = value

print("max", max_value)
print("min", min_value)
