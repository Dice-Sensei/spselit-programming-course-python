# Loops in code are important for executing the same set of instruction on more than one item or more than ones.

# Basically there are two types of loops: while and for loops
# For is mostly used for iterating over a sequence (list, tuple, string) or other iterable objects.
# While is mostly used when you don't know how many times you need to repeat the action.

# For loop structure is: keyword for the name of the variable which can be used inside loop and represents the current item, keyword in and iterable variable last symbol is ':'
# For loop is looping as long there are items in the iterable variable or is break-ed

my_number_list = [1, 2, 3, 4, 5]
print("Number list", my_number_list)

# Iterate over the number list and print its values
print("Iterating over number list:")
for number in my_number_list:
    print(number)

# Iterate over the number list and print only odd numbers
print("Iterating over number list and printing only odd numbers:")
for number in my_number_list:
    if number % 2 != 0:
        print(number)


# Iterate over the number string and print pairs of odd numbers
number_string = "73910462580273919468250731476985062958418734209619586734420681577689052304917682852604937315984068420759915038262708645149831706"
previous_number = None

print("Iterating over number string and printing pairs of odd numbers:")
for number in number_string:
    number = int(number)
    if number % 2 != 0:
        if previous_number is not None:
            print(f"{previous_number}{number}")

        previous_number = number
    else:
        previous_number = None


# Iterating over a large number of items created by range
print("Iterating over large number of items created by range:")
for number in range(0, 1000, 2):
    print(number)

# Range function here is a generator that means it generates values on the fly and does not store them all in memory - more on this later


# While loop structure is: keyword while bool condition and last symbol is ':'
# While loop is looping as long as bool condition is True or is break-ed

# Sum numbers from 1 to 10
print("Summing numbers from 1 to 10:")
number_sum = 0
current_number = 1

while current_number <= 10:
    number_sum += current_number
    current_number += 1

print(number_sum)


# If we need to exit the loop early, we can use the break keyword; works in both while and for loops
print("Summing numbers from 1 to 10 with break on 5:")
number_sum = 0
current_number = 1

while current_number <= 10:
    print(current_number)
    number_sum += current_number

    if current_number == 5:
        print("Breaking loop")
        break  # here we will break the loop when we reach 5

    current_number += 1

print(f"Sum: {number_sum}")

# If we need to skip some iterations, we can use continue keyword; works in both while and for loops
print("Summing numbers from 1 to 10 with continue on even numbers:")
number_sum = 0
current_number = 1

while current_number <= 10:
    print(current_number)
    if current_number % 2 == 0:
        print("Skipping even number")
        current_number += 1
        continue  # skip even numbers

    number_sum += current_number

    current_number += 1

print(f"Sum: {number_sum}")


# Common mistakes
# Infinite loop: forgetting to break loop or having always true condition
# Off-by-one errors: the range end is not included
