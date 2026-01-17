# Data collections - Set
# Set items are unordered, and does not allow duplicate values

# Sets can be created via more than one way
kebab_set = set("kebab")
kebab_set = {"kebab", "kebab s hranolkama", "zeleninu", "kebab"} # the same item "kebab" is not added multiple times

print(kebab_set)

kebab_set.add("tapas")
kebab_set.add("kebab")  # the same item "kebab" is not added multiple times

print(kebab_set)

asian_set = {"noodle", "kebab", "kebab s hranolkama", "noodle", "burger"}
print(asian_set)

# Set has many options for comparing data in sets
print(kebab_set.intersection(asian_set))

# They can be either written via functions or via operators
print(kebab_set | asian_set)

# Example of set usage - to get unique values from the list
my_list = [1, 2, 2, 3, 5, 8, 5, 3]
print(my_list)
print(set(my_list))
