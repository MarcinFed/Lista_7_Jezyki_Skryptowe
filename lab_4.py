def make_generator(function):
    def generator():
        index = 1
        while True:
            yield function(index)
            index +=1
    return generator()


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    fib = make_generator(fibonacci)
    for i in range(20):
        print(next(fib))

    arithmetic = make_generator(lambda n: 1 + (n - 1) * 3)
    for i in range(10):
        print(next(arithmetic))
