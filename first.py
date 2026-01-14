# proměná co se jmenuje x a přiřadím ji hodnotu 42
x = 42
print(x)
print(type(x))

# do stejné proměné si vložím jiný obsah a to jiný datovám typem (v Python povolono, jiné jazyky to nepodporují)
x = "hello"
print(x)
print(type(x))

# sum numbers
# tady dochází k "překrytí" vestavěné funkce sum právě vytvořenou proměnou
sum = 4 + 5
print(sum)

my_name = "Dice-Sensei"

print(my_name)

# sahám si na neexistující proměnou a program padá
# print(neexistujici_promena)

print(my_name)

x = 42
# tady proběhne nejdříve x + 1 a pak se výsledek vloží do nové proměné y
y = x + 1
print(y)

# tady se výsledek operace neukládá do proměné ale posílá se dál
print(x + 1)
