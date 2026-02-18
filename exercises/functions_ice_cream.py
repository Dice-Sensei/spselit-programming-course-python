# Úkolem je upgradovat stávající implementaci decisions_ice_cream.py
# - s využitím cyklu pro vyhodnocení všech kódů (nikoliv jejich jednotlivé zadávání)
# - s využitím funkcí


def char_is_in_collection(char, collection):
    return collection.count(char) > 0


def process_first_char(char):
    if char_is_in_collection(char, ("A", "B", "F")):
        return 8

    if char_is_in_collection(char, ("C", "D", "X")):
        return 9
    # 2 S check
    if char == "S":
        return 7

    return 10


def process_second_char(char):
    number = int(char)  # will always be number
    if 1 <= number <= 5:
        return 2
    elif 6 <= number <= 9:
        return 3
    elif number == 0:
        return -1

    # unexpected value
    raise ValueError()


def process_third_char(char, first_char):
    if char == "A":
        return 2
    elif char_is_in_collection(char, ("B", "C")):
        return 3
    elif char == first_char:
        return 5
    elif char == "Y" and first_char == "X":
        return -10

    return 1


def process_fourth_char(char):
    number = int(char)

    # 2 zero check
    if number == 0:
        return 5

    if number % 2 == 0:
        return 2

    return 3


def calculate_ice_cream_price(code):
    price_parts = []
    price = 0

    # 2 fix format
    code = code.upper()

    # 2 special checks
    if code == "X1X3":
        return 28

    if code.startswith("X1"):
        return 23

    # first char
    price_based_on_first_char = process_first_char(code[0])
    price += price_based_on_first_char
    price_parts.append(price_based_on_first_char)

    # second char (first number)
    price_based_on_second_char = process_second_char(code[1])
    price += price_based_on_second_char
    price_parts.append(price_based_on_second_char)

    # third char (second alphabet)
    price_based_on_third_char = process_third_char(code[2], code[0])
    price += price_based_on_third_char
    price_parts.append(price_based_on_third_char)

    # last char (last number)
    price_based_on_last_char = process_fourth_char(code[3])
    price += price_based_on_last_char
    price_parts.append(price_based_on_last_char)

    # check correctness
    if len(price_parts) != 4:
        raise ValueError("Incorrect length of price parts", price_parts)

    return price


def calculate_all_ice_cream_prices():
    ice_cream_codes = (
        "F3A2",
        "A1A5",
        "X0X6",
        "X1Y3",
        "C7F6",
        "K8B3",
        "S3C0",
        "K2H5",
        "X1X3",
        "X1H2",
        "l0a3",
    )

    for ice_cream_code in ice_cream_codes:
        print("Calculating price for " + ice_cream_code)
        print(calculate_ice_cream_price(ice_cream_code))


calculate_all_ice_cream_prices()
# Expected results: F3A2=14, A1A5=15, X0X6=15, X1Y3=23, C7F6=15, K8B3=19, S3C0=17, K2H5=16, X1X3=28, X1H2=23, l0a3=14
