from functools import reduce


number_list = [1, 2, 3, 4, 5, 6, 7]

# vynásobit number_list číslem 2
number_list_2x = []

for item in number_list:
    number_list_2x.append(item * 2)


def multiply_by_2(item):
    return item * 2


def is_odd(item):
    return item % 2 != 0


def accumulator(carry, item):
    return carry + item


print(list(map(multiply_by_2, number_list)))
print(list(filter(is_odd, number_list)))

print(list(map(multiply_by_2, filter(is_odd, number_list))))

print(reduce(accumulator, number_list))

print(reduce(accumulator, map(multiply_by_2, filter(is_odd, number_list))))

number_list_of_odds = filter(is_odd, number_list)
number_list_of_odds_multiplied_by_2 = map(multiply_by_2, number_list_of_odds)
sum_of_number_list_of_odds_multiplied_by_2 = reduce(
    accumulator, number_list_of_odds_multiplied_by_2
)

print(sum_of_number_list_of_odds_multiplied_by_2)


print(number_list_2x)


print(number_list)
