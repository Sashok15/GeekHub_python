# The function takes the function into the parameters and multiplies the value five times.
def decorator(func):
    def wrapper(*args):
        print("//////////////////")
        result = func(*args)
        print("//////////////////")
        return result * 5
    return wrapper


@decorator
def is_my_name(number):
    return number

print(is_my_name(20))


if __name__ == '__main__':
    pass
