# key - value pair
my_dictionary = {
    "hranolky": [40, 50, 60],
    "burger": 50,
    "noddle": 40,
}

print(my_dictionary)

print(my_dictionary["hranolky"])
print(my_dictionary.get("hranolky"))

my_dictionary["hranolky"] = 40  # nastavení hodnoty existujícímu klíči

my_dictionary["bagety"] = 80  # vytvoření nového key - value pair

print(my_dictionary)

my_dictionary.pop("burger")

print(my_dictionary)
