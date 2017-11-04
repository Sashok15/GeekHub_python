"""Write a script to concatenate N strings."""

a, b, c = 'aaa', 'bbb', 'ccc'


def concatenate_string(*args):
    k = ''
    for arg in args:
         k += arg
    return k
print(concatenate_string(a, b, c))
