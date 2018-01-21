""" Write a script to print out a set containing all the colours
    from color_list_1 which are not present in color_list_2.
        Test Data :
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        Expected Output :
        {'Black', 'White'} """

unique_colors = []
color_list_1 = {"White", "Black", "White", "Red", "Green"}
color_list_2 = {"Red", "Green"}
for color_1 in color_list_1:
    if color_1 not in color_list_2:
        unique_colors.append(color_1)
print(set(unique_colors))
