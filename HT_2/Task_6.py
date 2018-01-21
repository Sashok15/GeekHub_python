# The function takes the function into the parameters and multiplies the value five times.
def decorator(func):
    def wrapper(name):
        print("//////////////////")
        result = 'Your name: ' + name
        return result

    return wrapper


@decorator
def is_my_name(name):
    print(name)


print(is_my_name('sashka'))
