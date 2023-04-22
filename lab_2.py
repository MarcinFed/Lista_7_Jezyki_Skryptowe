def forall(pred, iterable):
    return all(pred(x) for x in iterable)


def exists(pred, iterable):
    return any(pred(x) for x in iterable)


def atleast(n, pred, iterable):
    return n <= sum(1 for x in iterable if pred(x))


def atmost(n, pred, iterable):
    return n >= sum(1 for x in iterable if pred(x))


if __name__ == "__main__":
    print(forall(lambda x: x % 3 == 0, [0, 1, 2, 3, 4]))
    print(forall(lambda x: x % 3 == 0, [0, 3]))
    print(exists(lambda x: x % 3 == 0, [0, 1, 2, 3, 4]))
    print(exists(lambda x: x % 3 == 0, [1, 2]))
    print(atleast(2, lambda x: x % 3 == 0, [0, 1, 2, 3, 4]))
    print(atleast(2, lambda x: x % 3 == 0, [0, 1]))
    print(atmost(2, lambda x: x % 3 == 0, [0, 1, 2, 3, 4, 6]))
    print(atmost(2, lambda x: x % 3 == 0, [0, 1]))
