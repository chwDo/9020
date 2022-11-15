from collections import Counter


# Given a nonnegative integer n, define 3 integers n*, n- and n+ as follows.
#
# Let n* be:
# - 0 if n contains no occurrence of an odd digit;
# - otherwise, the number consisting of ALL ODD DIGITS in n,
#   in INCREASING ORDER.
# For instance, if n is 29350459566388 then n* is 3355599.
#
# Let n- be n* with 1 replaced by 0
#                   3 replaced by 2
#                   ...
#                   7 replaced by 6
#                   9 replaced by 8
#   UNLESS n* starts with 1, in which case n- is 0.
# For instance, if n* is 3355599 then n- is 2244488.
#
# Let n+ be n* with 1 replaced by 2
#                   3 replaced by 4
#                   ...
#                   7 replaced by 8
#                   9 replaced by 0
#   UNLESS n* starts with 9, in which case n+ is 0.
# For instance, if n* is 3355599 then n+ is 4466600.
#
# Returns the triple (n*, n-, n+) as defined above.
# You can assume that n is a nonnegative integer.
def f(n):
    '''
    >>> f(2004280)
    (0, 0, 0)
    >>> f(1)
    (1, 0, 2)
    >>> f(9)
    (9, 8, 0)
    >>> f(5)
    (5, 4, 6)
    >>> f(23211)
    (113, 0, 224)
    >>> f(49909929)
    (99999, 88888, 0)
    >>> f(45445030303070033)
    (33333557, 22222446, 44444668)
    >>> f(889287767862576235673458)
    (33555777779, 22444666668, 44666888880)
    '''
    n_ = []
    if n == 0:
        return 0, 0, 0
    while (n > 0):
        x = n % 10
        n = n // 10
        if x % 2 != 0:
            n_.append(x)
    n_.sort()
    n_m = []
    n_p = []
    for i in n_:
        n_m.append(i - 1)
        n_p.append((i + 1) % 10)
    sum = sum1 = sum2 = 0
    for i in n_:
        sum = sum * 10
        sum += i

    if n_m != []:
        if n_m[0] == 0:
            sum1 = 0
        else:
            for i in n_m:
                sum1 = sum1 * 10
                sum1 += i

    if n_p != []:
        if n_p[0] == 0:
            sum2 = 0
        else:
            for i in n_p:
                sum2 = sum2 * 10
                sum2 += i
    return sum, sum1, sum2
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
