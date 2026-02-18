# Functions in code are used to add reusability (no need to write the same code many times) and for structuring/readability (it is easier to understand and maintain many small functions instead of one big)

# Functions should be small and do only one thing
# Functions should be named appropriately

# Definition of function
# Basic structure: def keyword name_of_function ():
def print_tree():
    # standard inner block code indention
    print("   *")
    print("  ***")
    print(" *****")
    print("*******")
    print("   |")

# Functions have to be called to run
# Functions has to be defined before they can be used
print_tree()

# Functions can be called multiple times
print_tree()
print_tree()

# Functions can be called from other functions
def print_forest():
    print_tree()
    print_tree()
    print_tree()

print("Printing forest:")
print_forest()


# Functions are automatically returning None value

print("Return value of print_tree():", print_tree())
print(type(print_tree()))

# By using the keyword return we can return value from the function
def return_hello():
    return "Hello!"

print("Return value of return_hello():", return_hello())
print(type(return_hello()))


# Functions can have defined params (inputs) to be more versatile
# Number of params is not limited, but for readability reasons it should be kept small
# Basic structure: def keyword name_of_function (param1, param2):
def sum_numbers(num1, num2):
    return num1 + num2

# When calling a function, arguments are passed to parameters

# Here we call a function by using position arguments - the order in which they are input is important
print(sum_numbers(5, 3))

# Here we call the same function using keyword arguments we define which param gets which value; order of arguments is not important
print(sum_numbers(num2=3, num1=5))

# Functions can also have default value for parameters - when no values is passed to them default will be used
# Basic structure: def keyword name_of_function (param1=def_value):
def greet(name, greeting="Welcome"):
    print(f"{greeting} {name}")

greet("Anna") # the default value for greeting will be used
greet("John", "Hello there") # greeting here is supplied, default value will not be used

# Functions can take two special parameters - *args and **kwargs
# *args collects extra positional arguments into a tuple
# **kwargs collects extra keyword arguments into a dictionary
# These can be used when we don't know how many arguments will be passed
# Or in decorators - in later lectures

def total_price(*prices):
    # inside special params are used without the * (star) at the start of their names
    print("RAW prices param:", prices)
    return sum(prices)

print("Total price =", total_price(2.5))
print("Total price =", total_price(2.5, 3.0, 4.75, 5.25))

def log_student_record(**student_record):
    print("RAW student_record param:", student_record)
    print("Student data:", student_record)

log_student_record(name="Maya", grade=9, club="Robotics")

# Order of arguments matters - params, *args, default params, **kwargs


# Functions can have inner functions - called nested functions
# These functions can be called only from the function they defined in

def outer_func(num1):
    def inner_func(inner_num1):
        print("Inner func")
        return inner_num1 + 5

    print("Outer func")
    return inner_func(num1 + 10)

print(outer_func(30))
# Note: show how inner_func is not offered and does not exist outside outer_func


# Scopes
# Scopes are regions (blocks of code) that share variables; respectively define what variables can be accessed from where
# Python creates scopes around functions only - other programming languages may have different scope areas

# Mostly we work with two scopes Global and Local
# Global - inside script body, accessible from anywhere
# Local - inside function, only accessible from it (or nested functions)

x = 42 # variable x on global scope

def scoped():
    y = 3 # variable y on local scope
    print("Inside function")
    print("x:", x) # accessing global variable
    print("y:", y) # accessing local variable

scoped()

print("x:", x) # accessing global variable
# Note: show how y is not available outside a scoped function


# System functions
# Python programming language has quite a few build-in functions like print(), sum(), len(), etc. - we already used them
# There are some system functions, which needs to be used or overridden for the system to work properly or to provide some functionality, for example __init__ in objects
