# def print_stars():
#     print("*********")


def star_decorator(func):
    # decorator pattern
    def wrap_func(*args, **kwargs):
        print("*********")
        result = func(*args, **kwargs)
        print("*********")
        return result

    return wrap_func


@star_decorator
def print_string(text):
    print(text)


@star_decorator
def sum_numbers(num1, num2):
    print(f"I am summing two numbers {num1} and {num2}")
    return num1 + num2


print_string("I was here phantomas")
print(sum_numbers(5, 8))

# def call_me(func):
#     func()


# print_me = print_stars
# print_me()

# print(type(print_me))
# print(print_me)

# call_me(print_stars)


# print_stars()
# print_string()
# print_stars()
