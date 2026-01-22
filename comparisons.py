# Decisions and flow through the program
# All decisions are based on bool / boolean values (even number comparison is first calculated and translated to boolean)

is_true = True  # it is true
is_false = False  # it is false

# Ask the user to write 'car' and compare if the user really wrote 'car'
user_input = input("Write 'car': ")
print("You wrote:", user_input)
print("It was expected 'car' input:", user_input == "car")

# Ask the user to write their age and compare if the user is 30 years old
# Comparison is allowed on different data types, but it may not work as expected - for that reason always use the same data type for comparison
# In this case int() is used to convert string input to integer for comparison (we are not checking if input was really a number which may lead to exception, but that is topic for other time)
user_input = input("Write your age: ")
print("You wrote:", user_input)
print("we are same old", int(user_input) == 30)

# Basic comparisons are:
# == means are equal
# != means are not equal
print("Is 3 == 4?", 3==4)
print("Is 3 != 4?", 3!=4)

# For numbers (integers, floats), we have additional comparisons:
# > means larger than
# >= means larger or equal to
# < means smaller than
# <= means smaller or equal to
print("Is 4 larger then 3?", 4 > 3)
print("Is 4 larger or equal to 3?", 4 >= 3)
print("Is 4 smaller then 3?", 4 < 3)
print("Is 4 smaller or equal to 3?", 4 <= 3)

# For objects, we have additional comparison:
# is - this one is comparing if variables are pointing to the same object in memory
shopping_cart = ["apple", "milk"]
shopping_cart2 = ["apple", "milk"]
print("Are equal (have same content)", shopping_cart == shopping_cart2)
print("Are same object (point to same place in memory)", shopping_cart is shopping_cart2)
# Note: for the lists to be equal, the order of items matters
