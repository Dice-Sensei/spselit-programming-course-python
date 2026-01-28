"""
Programming Course: For Loops and While Loops
High School Python Lecture Notes + Examples
"""

# -------------------------
# 1) Why loops?
# -------------------------
# Loops help you repeat actions without copying the same code many times.
# Example: print numbers 1 to 5.

my_number_list = [1, 2, 3, 4, 5]
print(my_number_list)

print("\n--- 1) Why loops? ---")
for number in my_number_list:
    print(number)

counter = 0
while counter < 5:
    print("Jsem úžasnej")
    counter += 1


user_input = input("Enter your name: ")
list_samohlasky = []
list_souhlasek = []
for character in user_input:
    print("Current character: ", character)
    if character in "aeiou":
        list_samohlasky.append(character)
    else:
        list_souhlasek.append(character)

print("User input parsed:")
print("Samohlasky: ", list_samohlasky)
print("Souhlasek: ", list_souhlasek)


car_manufacurer_list = ["Škoda", "BMW", "Volvo"]
# průchod položku po položce
for car in car_manufacurer_list:
    print(car)

for number in range(10, 20, 2):
    print(number)

for number in range(10):
    if number % 2 == 0:
        continue

    if number == 5:
        break

    print(number)

number_string = "73910462580273919468250731476985062958418734209619586734420681577689052304917682852604937315984068420759915038262708645149831706"

my_sum = 0
for number in number_string:
    number = int(number)

    if number == 7:
        continue

    if number == 3:
        continue

    print(number)

    if number % 2 == 0:
        my_sum += number

print(my_sum)

# # -------------------------
# # 3) for loop with range()
# # -------------------------
# # range(start, stop) goes from start up to (but not including) stop.
# # range(stop) starts from 0.
# # range can also take a step: range(start, stop, step).
# # - The step can be negative to count down.
# # - range produces numbers one by one without storing a full list.
#
# print("\n--- 3) for loop with range() ---")
# print("Numbers 0 to 4:")
# for i in range(5):
#     print(i)
#
# print("Numbers 1 to 5:")
# for i in range(1, 6):
#     print(i)
#
# print("Even numbers 2 to 10:")
# for i in range(2, 11, 2):
#     print(i)
#
# print("Counting down 5 to 1:")
# for i in range(5, 0, -1):
#     print(i)
#
#
# # -------------------------
# # 4) for loop over a list
# # -------------------------
# fruits = ["apple", "banana", "cherry"]
#
# print("\n--- 4) for loop over a list ---")
# print("Fruits:")
# for fruit in fruits:
#     print(fruit)
#
#
# # -------------------------
# # 5) Using a loop to sum numbers
# # -------------------------
# total = 0
# print("\n--- 5) Using a loop to sum numbers ---")
# for i in range(1, 6):  # 1+2+3+4+5
#     total = total + i
# print("Sum 1..5 =", total)
#
#
# # -------------------------
# # 6) while loop basics
# # -------------------------
# # A while loop keeps going as long as the condition is True.
# # The condition is checked before each iteration.
# # If it is False at the start, the loop does not run at all.
# # Use a clear condition when you can say "keep going while ...".
# # Use break when the stopping moment is discovered inside the loop body.
#
# count = 1
# print("\n--- 6) while loop basics ---")
# print("Counting with while:")
# while count <= 5:
#     print(count)
#     count = count + 1
#
#
# # -------------------------
# # 7) while loop with user input
# # -------------------------
# # Keep asking until the correct password is typed.
#
# password = "python123"
# guess = ""
# print("\n--- 7) while loop with user input ---")
# while guess != password:
#     guess = input("Type the password: ")
#     if guess != password:
#         print("Wrong password, try again.")
#     else:
#         print("Access granted!")
#
#
# # -------------------------
# # 8) break and continue
# # -------------------------
# # break stops the loop completely.
# # continue skips to the next iteration.
#
# print("\n--- 8) break and continue ---")
# print("Break example:")
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
#
# print("Continue example (odd numbers only):")
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)
#
#
# # -------------------------
# # 9) Common mistakes
# # -------------------------
# # 1) Infinite loop: forgetting to update the variable.
# # 2) Off-by-one errors: range end is not included.
#
# print("\n--- 9) Common mistakes ---")
# # Example of potential infinite loop (commented out):
# # n = 1
# # while n <= 5:
# #     print(n)
# #     # n = n + 1  # if this line is missing, loop never ends!
#
#
# # -------------------------
# # 10) Which loop to use?
# # -------------------------
# # Use a for loop when:
# # - You know how many times you will repeat.
# # - You want to go through each item in a list, string, or range.
# #
# # Use a while loop when:
# # - You do not know how many repeats are needed.
# # - You are waiting for a condition to become True or False.
# # - You are taking input until a correct value is entered.
# #
# # Rule of thumb: If you can describe it as "for each item" or "for N times",
# # choose for. If it is "until this happens", choose while.
#
# print("\n--- 10) Which loop to use? ---")
#
#
# # -------------------------
# # 11) Practice tasks for students
# # -------------------------
# print("\n--- 11) Practice tasks for students ---")
# # 1) Print numbers 10 to 1 using a while loop.
# # 2) Print the squares of numbers 1 to 5 using a for loop.
# # 3) Sum all even numbers from 1 to 20.
# # 4) Ask the user for numbers until they type 0, then print the total.
