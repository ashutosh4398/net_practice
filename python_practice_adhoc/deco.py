import time


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def some_func(n):
    # db query
    time.sleep(2)
    return n

@cache
def some_func_2(n):
    # db query
    time.sleep(2)
    return n



# deco = cache(some_func)
# print(deco(1))
# print(deco(1))
# print(deco(2))
# print(some_func(1))
# print(some_func(1))
# print(some_func_2(1))
# print(some_func_2(1))