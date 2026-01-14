# kolekce, která nemá pevně definované pořadí, všechny musí být unikátní
# kebab_set = set("kebab")
kebab_set = {"kebab", "kebab s hranolkama", "zeleninu", "kebab"}

print(kebab_set)

kebab_set.add("tapas")
kebab_set.add("kebab")  # přidávání stejné položky, nic neudělá

print(kebab_set)

asian_set = {"noodle", "kebab", "kebab s hranolkama", "noodle", "burger"}
print(asian_set)

print(kebab_set.intersection(asian_set))

print(kebab_set | asian_set)

# get unique values from list via set
my_list = [1, 2, 2, 3, 5, 8, 5, 3]
print(my_list)
print(set(my_list))
