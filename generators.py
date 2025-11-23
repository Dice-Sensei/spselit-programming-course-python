# # via list
# list = list(range(10000000))

# for i in list:
#     print(i)

# # via generator
# for j in range(10000000):
#     print(i)


# def generate_numbers(start, end):
#     number = start
#     while number <= end:
#         yield number
#         # print(number)
#         number += 1


# gen = generate_numbers(1, 20)

# print(next(gen))
# print(next(gen))

# print(next(gen))

# print(next(gen))

# print("for now")

# for x in gen:
#     print(x)


# def fibonacci_generator():
#     sequence_number = 0
#     prev2 = 0
#     prev1 = 1

#     while True:
#         if sequence_number == 0:
#             yield 0
#             sequence_number += 1
#             continue

#         if sequence_number == 1:
#             yield 1
#             sequence_number += 1
#             continue

#         current = prev1 + prev2

#         yield current

#         prev2 = prev1
#         prev1 = current

#         sequence_number += 1


# gen = fibonacci_generator()

# print(next(gen))  # f0
# print(next(gen))  # f1
# print(next(gen))  # f3 ...
# print(next(gen))  # f4

# x = 1

# while x < 20:
#     print(next(gen))
#     x += 1


def fib():
    a = 0
    b = 1

    while True:
        yield a

        temp = a
        a = b
        b = temp + a


gen = fib()

print(next(gen))  # f0
print(next(gen))  # f1
print(next(gen))  # f3 ...
print(next(gen))  # f4

x = 1

while x < 20:
    print(next(gen))
    x += 1
