# vytvoření proměné = datový typ je list

car_manufacturers_list = []
print(car_manufacturers_list)
print(type(car_manufacturers_list))

# car_manufacturers_list = list()
car_manufacturers_list = ["Škoda", "BMW", "Volvo"]
print(car_manufacturers_list)
print(type(car_manufacturers_list))

# ukázka, že v případě objektů při jejich přiřazení nedochází ke kopírování ale pouze odkazování na ten stejný
not_copy = car_manufacturers_list
print(not_copy)

car_manufacturers_list[0] = ""
print(car_manufacturers_list)
print(not_copy)


print(car_manufacturers_list)
# na položky se přistupuje pomocí indexů (od 0)
print("první položka listu" + car_manufacturers_list[0])
print("druhá položka listu" + car_manufacturers_list[1])

print(len(car_manufacturers_list))

# přepsání hodnoty
car_manufacturers_list[0] = "Škoda"
print(car_manufacturers_list)

# vypsání posledního položky
print(car_manufacturers_list[len(car_manufacturers_list) - 1])  # délka - 1
print(car_manufacturers_list[-1])

# přidáme si do listu položku - jde na konec
car_manufacturers_list.append("Mercedes Benz")
print(car_manufacturers_list)

car_manufacturers_list.sort()
print(car_manufacturers_list)

# okopírovat list
# new_list = car_manufacturers_list #NEFUNGUJE - pouze se předá odkaz na stejnej list

new_list = car_manufacturers_list.copy()  # really makes copy
print("new list via copy", new_list)

new_list2 = car_manufacturers_list[::]
print("new list via [::]", new_list2)

car_manufacturers_list[0] = "0"

print("old modified list", car_manufacturers_list)
print("new list via copy", new_list)
print("new list via [::]", new_list2)

# kolikrát se něco nachází v listu
print(car_manufacturers_list)
print(car_manufacturers_list.count("0"))

# zda list obsahuje položky
print(any(car_manufacturers_list))
