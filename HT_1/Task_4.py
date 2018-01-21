"""Write a script to concatenate N strings."""

a, b, c = 'aaa', 'bbb', 'ccc'


def concatenate_string(*args):
    string = ''
    for arg in args:
        string += arg
    return string


print(concatenate_string(a, b, c))
