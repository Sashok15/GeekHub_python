""" Write a script to remove duplicates from Dictionary. """

dic = {1: 10, 2: 25, 3: 30, 4: 25, 5: 20}
res_dic = {}
for key, value in dic.items():
    if value not in res_dic.values():
        res_dic[key] = value
print(res_dic)


if __name__ == "__main__":
    pass