# Decorators are special functions that may modify or extend the behavior of other functions

# Basic structure:
# Function, which will be used as a decorator which accepts one parameter, which is a decorated function
# Called decorator pattern
def star_decorator(func):
    # wrapper function which accepts *args and **kwargs
    def wrap_func(*args, **kwargs):
        print("*********") # custom code of decorator
        result = func(*args, **kwargs) # call of decorated function with provided params, note: stars in front of params are passed too; saving result to variable
        print("*********") # custom code of decorator
        return result # returning a result of a decorated function

    return wrap_func # returning wrapper function


@star_decorator # use of decorator
def print_string(text):
    print(text)

# Standard function with added decorator
# This function has parameters; And they are passed correctly thanks to the decorator pattern
@star_decorator
def sum_numbers(num1, num2):
    print(f"I am summing two numbers {num1} and {num2}")
    return num1 + num2

# standard call of functions - here is no change related to decorators
print_string("I was here phantomas")
print(sum_numbers(5, 8))


# Python has some built-in decorators like @cache
