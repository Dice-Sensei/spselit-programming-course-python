"""
Programming Course: Functions
High School Python Lecture Notes + Examples
"""

# -------------------------
# 1) Why functions?
# -------------------------
# Functions let you group code into a reusable block.
# They help avoid repetition and make programs easier to read.

print("\n--- 1) Why functions? ---")


# -------------------------
# 2) Basic function definition and call
# -------------------------
# def creates a function. The body is indented.
# You must call the function to run it.
# Indentation shows which lines belong to the function body.
# If a line is not indented, it is outside the function.
# Python uses indentation instead of { } braces.
# A common choice is 4 spaces per indent level.

print("\n--- 2) Basic function definition and call ---")

def say_hello():
    print("Hello!")

say_hello()
say_hello()


# -------------------------
# 3) Parameters and arguments
# -------------------------
# A parameter is a variable in the function definition.
# An argument is the value you pass when calling the function.

print("\n--- 3) Parameters and arguments ---")

def greet(name):
    print("Hello,", name)

greet("Anna")
greet("Omar")


# -------------------------
# 4) Returning values
# -------------------------
# return sends a value back to the caller.
# After return, the function stops.

print("\n--- 4) Returning values ---")

def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)


# -------------------------
# 5) Using return in calculations
# -------------------------

print("\n--- 5) Using return in calculations ---")

def rectangle_area(width, height):
    return width * height

area = rectangle_area(4, 6)
print("Area =", area)
print("Double area =", rectangle_area(4, 6) * 2)


# -------------------------
# 6) Default parameter values
# -------------------------
# If you do not pass a value, the default is used.

print("\n--- 6) Default parameter values ---")

def power(base, exponent=2):
    return base ** exponent

print("5 squared =", power(5))
print("2 cubed =", power(2, 3))


# -------------------------
# 7) *args and **kwargs (extra arguments)
# -------------------------
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra keyword arguments into a dictionary.
# Use them when you do not know how many arguments will be passed.
# Positional arguments come first (by position), keyword arguments use name=value.
# You can mix them in a call, but positional must come before keyword.
# Inside the function, args behaves like a tuple and kwargs like a dict.

print("\n--- 7) *args and **kwargs (extra arguments) ---")

def total_price(*prices):
    return sum(prices)

def create_student_record(**info):
    # Builds and prints a student record from labeled details.
    print("Student record:", info)

print("Total price =", total_price(2.5, 3.0, 4.75))
create_student_record(name="Maya", grade=9, club="Robotics")


# -------------------------
# 8) Multiple parameters and clear names
# -------------------------

print("\n--- 8) Multiple parameters and clear names ---")

def format_full_name(first_name, last_name):
    return first_name + " " + last_name

print(format_full_name("Lina", "Park"))


# -------------------------
# 9) Return vs print
# -------------------------
# print shows a value; return gives it back to the caller.
# You can use return value later, but you cannot reuse print output.

print("\n--- 9) Return vs print ---")

def multiply(a, b):
    return a * b

print("Printed:", multiply(2, 4))
saved = multiply(2, 4)
print("Saved for later:", saved + 1)


# -------------------------
# 10) Variable scope (local vs global)
# -------------------------
# Variables created inside a function are local.
# They exist only inside that function and are not visible outside.
# Variables created outside a function are global.
# If a local variable has the same name as a global one, the local one wins.

print("\n--- 10) Variable scope (local vs global) ---")

def make_message():
    message = "Inside the function"
    print(message)

make_message()


# -------------------------
# 11) Function design tips
# -------------------------
# - Give functions clear names using verbs.
# - Keep each function focused on one job.
# - Use return when you want to compute a result.

print("\n--- 11) Function design tips ---")


# -------------------------
# 12) Practice tasks for students
# -------------------------
print("\n--- 12) Practice tasks for students ---")
# 1) Write a function that prints "Good morning".
# 2) Write a function that returns the square of a number.
# 3) Write a function that takes two numbers and returns the larger one.
# 4) Write a function that returns the sum of numbers from 1 to n.
