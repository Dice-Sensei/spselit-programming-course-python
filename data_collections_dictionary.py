# Data collections - Dictionary
# Dictionary stores items as key-value pair
# Dictionary items are ordered, changeable, and does not allow duplicate keys

# Dictionaries can be created via more than one way
my_dictionary = dict()
my_dictionary = {
    "hranolky": [40, 50, 60],
    "burger": 50,
    "noddle": 40,
}

print(my_dictionary)

# Items in the dictionary are accessed via keys
print(my_dictionary["hranolky"])
print(my_dictionary.get("hranolky"))

# Updating values and adding new ones is done with the same code
my_dictionary["hranolky"] = 40  # setting value to existing key
my_dictionary["bagety"] = 80  # creating new key - value pair

print(my_dictionary)

# Removing items from the dictionary
my_dictionary.pop("burger")

print(my_dictionary)
