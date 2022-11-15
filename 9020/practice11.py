from math import sqrt, floor


def find_all_prime_under_n(n):
    L = [True] * (n + 1)
    L[0] = L[1] = False
    for i in range(2, floor(sqrt(n))):
        if not L[i]:
            continue
        else:
            for j in range(i * i, n + 1, i):
                L[j] = False
    return L


# def is_prime(n):
#     # Only used to test odd numbers.
#     return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))
#
#
# print('The solutions are:\n')
# # The list of all even i's such that a + i is one of
# # a, b, c, d, e, f.
# good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
# for a in range(10_001, 100_000 - good_leaps[-1], 2):
#     # i should be in good_leaps iff a + i is prime
#     # for i = 0, 2, 4, ..., 30.
#     if all(((i in good_leaps) == is_prime(a + i))
#                for i in range(0, good_leaps[-1] + 1, 2)
#           ):
#         print(' '.join((str(a + i) for i in good_leaps)))


print('The solutions are:\n')
# The list of all even i's such that a + i is one of a, b, c, d, e, f.
L = find_all_prime_under_n(99999)
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
print(good_leaps)
for n in range(10_001, 100_000 - 30, 2):
    # if all(L[i] for i in good_leaps):
    #     if all(not L[j] for j in range(n,n+30) if j not in good_leaps):
    if all(((i in good_leaps) == L[n + i]) for i in range(0, good_leaps[-1] + 1, 2)):
        print(' '.join((str(n + i) for i in good_leaps)))
