""" Write a script to concatenate following dictionaries to create a new one.
        Sample Dictionary :
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50,6:60}
        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}


def update_dict(*dict_):
    dictionary = {}
    for elem in dict_:
        dictionary.update(elem)
    return dictionary


print(update_dict(dict1, dict2, dict3))
