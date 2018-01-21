""" Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False """

num = int(input())

numbers = [i for i in range(1, 10)]
if num in numbers:
    print("True")
else:
    print("False")
