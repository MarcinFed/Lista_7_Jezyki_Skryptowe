from functools import reduce


def acronym(words):
    return reduce(lambda acc, word: acc + word[0], words, "")


def median(numbers):
    sorted_num = sorted(numbers)
    num_length = len(numbers)
    median_index = num_length // 2

    return(sorted_num[median_index - 1] + sorted_num[median_index]) / 2 if num_length % 2 == 0 else sorted_num[median_index]


def newton_sqrt(x, epsilon):
    def check_epsilon(result):
        return abs(result**2 - x) < epsilon

    def next_result(result):
        return (result + x / result) / 2

    def check_result(result):
        return result if check_epsilon(result) else check_result(next_result(result))

    return check_result(1)


def get_alphabetical_dict(entry):
    words = entry.split()
    return reduce(lambda acc, w: reduce(lambda acc_2, c: {**acc_2, c.lower(): acc_2.get(c.lower(), [])+[w]} if c.isalpha() else acc_2, w, acc), words, {})


def flatten(entry_list):
    result = []
    for item in entry_list:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(acronym(["Narodowy", "Fundusz", "Zdrowia"]))
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))
    print(newton_sqrt(3, epsilon=0.1))
    print(get_alphabetical_dict("on i ona"))
    print(flatten([1, [2, 3], [[4, 5], 6]]))
    

