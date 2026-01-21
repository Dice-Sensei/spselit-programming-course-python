name_list = ["Erik", "Jirka", "Dominik", "Tomáš"]
print(name_list)

name_list.append("Artem")
print(name_list)

name_list.extend(["Honza", "Jakub"])
print(name_list)

name_list.extend(
    "Karel"
)  # nesprávné použití - string je sice iterable, takže je použitelný ale znamená to že pro každé písmeno se přidá záznam
print(name_list)
