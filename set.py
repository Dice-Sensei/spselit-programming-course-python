kebab_set = {"kebab", "kebab s hranolkama", "zeleninu", "kebab"}

print(kebab_set)

kebab_set.add("tapas")
kebab_set.add("kebab")

print(kebab_set)

asian_set = {"noodle", "kebab", "kebab s hranolkama", "noodle", "burger"}
print(asian_set)

print(kebab_set.intersection(asian_set))

print(kebab_set | asian_set)