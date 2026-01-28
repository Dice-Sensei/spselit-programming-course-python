# Výpočet ceny zmrzliny z jejího kódu
# Příklad kódu: E3N2
# Způsob kódování písmeno číslo písmeno číslo

# Pokud počáteční písmeno je A nebo B nebo F => základ ceny je 8
# Pokud počáteční písmeno je C nebo D nebo X => základ ceny je 9
# Pokud počáteční písmeno je jiné než výšše zmíněné => základ ceny je 10

# Pokud první číslo je 1-5 => k ceně se přičítá 2
# Pokud první číslo je 6-9 => k ceně se přičítá 3
# Pokud první číslo je 0 => od ceny se odečítá 1

# Pokud druhé písmeno je A => k ceně se přičítá 2
# Pokud druhé písmeno je B nebo C => k ceně se přičítá 3
# Pokud druhé písmeno se rovná prvnímu => k ceně se přičítá 5
# Pokud druhé písmeno je Y a první je X = od ceny se odečítá 10
# Pokud neplatí ani jedna z podmínek pro druhé písmeno => k ceně se přičítá 1

# Pokud poslední číslice je sudá => k ceně se přičítá 2
# Pokud poslední číslice je lichá => k ceně se přičítá 3

# Kolik stojí následující zmrzliny? F3A2, A1A5, X0X6, X1Y3, C7F6, K8B3
#2 S3C0, K2H5, X1X3, X1H2, l0a3

code = "X0X6"
price = 0
price_parts = []

# first char
if code[0] == "A" or code[0] == "B" or code[0] == "F":
    price = 8
    price_parts.append(8)
elif code[0] == "C" or code[0] == "D" or code[0] == "X":
    price = 9
    price_parts.append(9)
else:
    price = 10
    price_parts.append(10)

# first number
first_number = int(code[1])
if 1 <= first_number <= 5:
    price += 2
    price_parts.append(2)
elif 6 <= first_number <= 9:
    price += 3
    price_parts.append(3)
elif first_number == 0:
    price -= 1
    price_parts.append(-1)
else:
    raise ValueError()

# second char
if code[2] == "A":
    price += 2
    price_parts.append(2)
elif code[2] == "B" or code[2] == "C":
    price += 3
    price_parts.append(3)
elif code[2] == code[0]:
    price += 5
    price_parts.append(5)
elif code[2] == "Y" and code[0] == "X":
    price -= 10
    price_parts.append(-10)
else:
    price += 1
    price_parts.append(1)

# last number
last_number = int(code[3])
if last_number % 2 == 0:
    price += 2
    price_parts.append(2)
else:
    price += 3
    price_parts.append(3)

print(price)
print(price_parts)  # check for correct length
print(sum(price_parts))

# Results: F3A2=14, A1A5=15, X0X6=15, X1Y3=4, C7F6=15, K8B3=19,