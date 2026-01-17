# Data collections - List
# List items are ordered, changeable, and allow duplicate values

# Lists can be created via more than one way
car_manufacturers_list = list()
car_manufacturers_list = ["Škoda", "BMW", "Volvo"] #preffered way - for readability
print(car_manufacturers_list)
print(type(car_manufacturers_list))

# Items in the list are accessible via index (starting from 0)
print("First item of list" + car_manufacturers_list[0])
print("Second item of list" + car_manufacturers_list[1])

# Built-in function len can be used to get the length of the list
print(len(car_manufacturers_list))

# We can not only access the values, but we can also modify them
car_manufacturers_list[0] = "Škoda"
print(car_manufacturers_list)

# Printing of the last item
print(car_manufacturers_list[len(car_manufacturers_list) - 1])  # length of the list -1 - standard way how to write it
print(car_manufacturers_list[-1]) # Python specific

# Adding items to the list - items are put on the end
car_manufacturers_list.append("Mercedes Benz")
print(car_manufacturers_list)

# Using build-in method to sort the list
print("Unsorted list", car_manufacturers_list)
car_manufacturers_list.sort()
print("Sorted list", car_manufacturers_list)

# Using build-in method to count the occurrences of an item in the list
print("How many times does the list contains item 0?", car_manufacturers_list.count("0"))

# Using build-in function to check if the list contains any items
print("Does the list contain any items?", any(car_manufacturers_list))

# Showcase of the behavior of objects in memory related to their copying
not_copy = car_manufacturers_list # this won't make copy this will just create a new variable pointing to the same list in memory
print(not_copy)

car_manufacturers_list[0] = "X" # so when one of the variables is modified, both will show the same changes
print("Original variable", car_manufacturers_list)
print("Not a copy variable", not_copy)

# Real copying of lists
new_list = car_manufacturers_list.copy()  # using build-in copy method
print("new list via copy", new_list)

new_list2 = car_manufacturers_list[::] # using slicing - Python specific
print("new list via slicing", new_list2)

car_manufacturers_list[0] = "0"

print("old modified list", car_manufacturers_list)
print("new list via copy", new_list)
print("new list via slicing", new_list2)