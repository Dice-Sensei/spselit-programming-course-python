# 1! = 1
# 2! = 2 x 1!
# 3! = 3 x 2!


# 5! = 1*2*3*4*5
# def factorial_loop(number_to_factorial):
#     current = 1
#     result = 1
#     while True:

#         result = result * current
#         current += 1

#         if current > number_to_factorial:
#             return result


# 5! = 5 * 4 * 3 * 2 * 1
from functools import cache


@cache
def factorial_recursion(number_to_factorial):
    print(f"{number_to_factorial}!")

    if number_to_factorial < 0:
        raise ValueError("Factorial of number < 0 is not possible!")

    if number_to_factorial == 0 or number_to_factorial == 1:
        return 1

    return number_to_factorial * factorial_recursion(number_to_factorial - 1)


# print(factorial_loop(5))
print(factorial_recursion(5))
print(factorial_recursion(3))
print(factorial_recursion(8))
