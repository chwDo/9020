from random import seed, shuffle
from timeit import timeit


# for_seed is meant to be an integer, length a strictly positive integer.
# length will not be large for most tests, but can be as large as 10_000_000.


def generate_permutation(for_seed, length):
    seed(for_seed)
    values = list(range(1, length + 1))
    shuffle(values)
    global L
    L = [0] + [1] * length
    return values


def maps_to(values, x):
    return (values.index(x) + 1)


def length_of_cycle_containing(values, x):
    answer_list = []
    index = values.index(x)
    while x != values[x - 1]:
        answer_list.append(x)
        values[index], values[x - 1] = values[x - 1], values[index]
        x = values[index]
    answer_list.append(values[index])
    _len = len(answer_list)
    for _ in answer_list:
        L[_] = _len
    return _len


def analyse(values):
    for x in values:
        if x != values[x - 1]:
            length_of_cycle_containing(values, x)
    return L


if __name__ == '__main__':
    values = generate_permutation(10, 10_000_000)
    print(timeit('analyse(values)', number=1, globals=globals()))
    print(L[500])
