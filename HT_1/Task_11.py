""" Write a script to remove duplicates from Dictionary. """

dictionary = {1: 10, 2: 25, 3: 30, 4: 25, 5: 20}
res_dict = {}
for key, value in dictionary.items():
    if value not in res_dict.values():
        res_dict[key] = value
print(res_dict)
