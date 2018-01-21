""" Write a script to remove an empty tuple(s) from a list of tuples
    Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] """
data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
data = [i for i in data if i != ()]
print(data)
