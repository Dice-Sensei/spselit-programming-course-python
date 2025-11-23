from time import time


def performance_counter(func):
    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        difference = finish - start
        print(f"Function took: {difference}s")
        return result

    return wrap


@performance_counter
def create_list(count):
    values = list(range(count))


create_list(10000)
create_list(100000)
create_list(1000000)  # 1M
create_list(10000000)
create_list(100000000)
# create_list(1000000000)
