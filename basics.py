# Create variable x and assign it value 42 (integer)
x = 42

# Print (to console) variable x via build in function
print(x)

# Print type of variable x via type build in function
print(type(x))

# Assign a new value to variable x; the new value is of string data type
# Python supports assigment of different data types to the same variable (some other languages don't)
x = "hello"

print(x)
print(type(x))

# Other basic data types are float for floating point numbers and bool for boolean values (True/False)
x = 3.14
print(x)
print(type(x))

x = True
print(x)
print(type(x))

# Here are happening two things first we are calculating 4 + 5 and then assigning it to variable sum
#  Also, we are "shadowing" built-in function sum - which means we are reusing name of built-in function for our own variable; This is not recommended and some other languages don't support it
sum = 4 + 5
print(sum)

# Here we are doing the same calculating 4 + 5 as above but without assigning it to variable before printing - which means that we can't access it later
print(4 + 5)

# Here we are trying to print variable my_name which is not defined yet - and this will cause an error
# It is commented out so the error does not occur
# print(neexistujici_promena)
