from functools import lru_cache
from lab_4 import fibonacci


def make_generator_mem(function):
    @lru_cache()
    def memoized_function(n):
        return function(n)

    def generator():
        index = 1
        while True:
            yield memoized_function(index)
            index += 1

    return generator()


if __name__ == "__main__":
    fibonacci_gen = make_generator_mem(fibonacci)
    for i in range(20):
        print(next(fibonacci_gen))
