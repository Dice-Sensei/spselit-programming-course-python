from functools import reduce


number_list = [1, 2, 3, 4, 5, 6, 7]


print(
    reduce(
        lambda carry, item: carry + item,
        map(lambda item: item * 2, filter(lambda item: item % 2 != 0, number_list)),
    )
)
