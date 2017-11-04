from random import randint, uniform
import time

list_int = []
list_float = []


def generate_list():
    for i in range(10000):
        list_int.append(randint(0, 99))
        list_float.append(uniform(0, 99))

generate_list()

# create a copies int lists for each sort function
list_int_selection_sort = list_int[:]
list_int_insertion_sort = list_int[:]
list_int_bubble_sort = list_int[:]


# create a copies float lists for each sort function
list_float_selection_sort = list_float[:]
list_float_insertion_sort = list_float[:]
list_float_bubble_sort = list_float[:]

# use default sort for int
list_int_default_sort = list_int[:]
list_int_default_sort.sort()

# use default sort for float
list_float_default_sort = list_float[:]
list_float_default_sort.sort()


def selection_sort(arr):
    start_time = time.time()
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[k]:
                k = j
        if k != i:
            var = arr[k]
            for n in range(k, i-1, -1):
                arr[n] = arr[n-1]
            arr[i] = var
    end_time = time.time()
    my_time = end_time - start_time
    return my_time


def insertion_sort(arr):
    start_time = time.time()
    if len(arr) == 0:
        return arr
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    end_time = time.time()
    my_time = end_time - start_time
    return my_time


def bubble_sort(arr):
    start_time = time.time()
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    end_time = time.time()
    my_time = end_time - start_time
    return my_time

selection_time = selection_sort(list_int_selection_sort)
insertion_time = insertion_sort(list_int_insertion_sort)
bubble_time = bubble_sort(list_int_bubble_sort)

selection_time_f = selection_sort(list_float_selection_sort)
insertion_time_f = insertion_sort(list_float_insertion_sort)
bubble_time_f = bubble_sort(list_float_bubble_sort)


def check_list():
    if list_int_default_sort == list_int_selection_sort:
        print("Selection_sort: time = {0:{f}}, the list is sorted correctly = true"
              .format(selection_time, f='.4f'))
    else:
        print("the list is sorted correctly = false")

    if list_float_default_sort == list_float_selection_sort:
        print("Selection_sort for float: time = {0:{f}}, the list is sorted correctly = true"
              .format(selection_time_f, f='.4f'))
    else:
        print("the list is sorted correctly = false")
    print()

    # compare insertion_sort for int and float
    if list_int_default_sort == list_int_insertion_sort:
        print("Insertion_sort: time = {0:{f}}, the list is sorted correctly = true"
              .format(insertion_time, f='.4f'))
    else:
        print("the list is sorted correctly = false")

    if list_float_default_sort == list_float_insertion_sort:
        print("Insertion_sort for float: time = {0:{f}}, the list is sorted correctly = true"
              .format(insertion_time_f, f='.4f'))
    else:
        print("the list is sorted correctly = false")
    print()

    # compare bubble_sort for int and float
    if list_int_default_sort == list_int_bubble_sort:
        print("Bubble_sort: time = {0:{f}}, the list is sorted correctly = true"
              .format(bubble_time, f='.4f'))
    else:
        print("the list is sorted correctly = false")

    if list_float_default_sort == list_float_bubble_sort:
        print("Bubble_sort for float: time = {0:{f}}, the list is sorted correctly = true"
              .format(bubble_time_f, f='.4f'))
    else:
        print("the list is sorted correctly = false")


check_list()
