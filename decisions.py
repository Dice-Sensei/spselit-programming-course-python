# Decisions in code are important for controlling the flow of the program based on certain conditions.
# For that we can use if statements (or if-else statements)

# Example: Can you drink?
print("Can you drink?")
legal_drinking_age = 18
my_age = int(input("Enter your age: "))

if my_age >= legal_drinking_age:
    # this part will be executed only when the condition is true
    print("Yes, you can!")
    print("Let's go party!")
else:
    # this part will be executed only when the condition is false
    print("No, you can't!")

# this is not part of if statement and will be executed regardless of the condition
print("END")

# In if statements (and other constructions too), the indentation of inner blocks is really important - that is how Pythons know it is an inner block in this project it is set to 4 spaces
# Other languages are using mostly {} to delimit blocks

# The only required part of the if statement is if and inner block for if, other parts like else are optional
# Example: When you see the cat call for it
see_cat = True
if see_cat:
    print("pspsppsps")

# In this example there is no else block as it does not make sense to do anything when you don't see a cat

# Example: Go for a car ride if you have a car and driving license
# In case we need to check more conditions we can either

# Sometimes it is good to use not equal instead of negating equal
# print("Is 3 not equal to 4?", 3 != 4)
# print("Is 3 not equal to 4?", not (3 == 4))
# 3 != 4 # používanější varianta

# # print(bool(" ")) #don't use for now
#

# have_car = False
# have_driving_license = False
#
# print("ride?")
#
# if not have_car:
#     print("Get car first")
# elif have_driving_license == False:
#     print("Get driving license")
# else:
#     print("Let's go for a ride!")
#
# # stejný zápis jako vejš ale bez elif - tady je horší čitelnost kvůli zanoření
# if not have_car:
#     print("Get car first")
# else:
#     if have_driving_license == False:
#         print("Get driving license")
#     else:
#         print("Let's go for a ride!")
#
#
# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# else:
#     print("You either don't have a car or license")
#
# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# else:
#     if not have_car:
#         print("Get car first")
#
#     if not have_driving_license:
#         print("Get license")
#
# a = 40
#
# if 40 < a < 65:
#     print("Is in")
#
# if a > 40 and a < 65:
#     print("Is in")

# if have_car and have_driving_license:
#     print("Let's go for a ride!")
# elif not have_car:
#     print("Get car first")
# elif not have_driving_license:
#     print("Get driving license")
#
#
# beer_in_fridge = True
# beer_in_basement = True
# beer_in_cupboard = True
#
# print("Do I have a beer at home?")
# if beer_in_fridge or beer_in_basement or beer_in_cupboard:
#     print("Yes I do!")
# else:
#     print("Let's go shopping!")
#
#
# ice_cream_found = False

# if ice_cream_found and spoon: #short circuit spoon is not checked because first part was True
#     print('let s have ice cream')
