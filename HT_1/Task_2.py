""" Write a script to print out a set containing all the colours
    from color_list_1 which are not present in color_list_2.
        Test Data :
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        Expected Output :
        {'Black', 'White'} """

a = []
color_list_1 = {"White", "Black", "White", "Red", "Green"}
color_list_2 = {"Red", "Green"}
for i in color_list_1:
    if i not in color_list_2:
        a.append(i)
print(set(a))
