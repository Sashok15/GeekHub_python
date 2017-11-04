""" Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False """

s = int(input())

a = [i for i in range(1, 10)]
if s in a:
    print("True")
else:
    print("False")