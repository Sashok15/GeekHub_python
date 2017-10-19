""" Write a script to remove an empty tuple(s) from a list of tuples
    Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] """
li = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
li = [i for i in li if i != ()]
print(li)


if __name__ == "__main__":
    pass