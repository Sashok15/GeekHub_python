"""Write a script to get the maximum and minimum value in a dictionary."""

dictionary = {1: 7, 2: 0, 3: 7, 4: 24, 5: -3, 6: -10}
k = dictionary[1]
m = dictionary[1]
for key, value in dictionary.items():
    if value >= k:
        k = value
    elif value < m:
        m = value

print("max", k)
print("min", m)


if __name__ == "__main__":
    pass