from math import sqrt, floor
from timeit import timeit
from itertools import compress
def is_good_prime(number):
    if 0 < number <= 3:
        return True
    str_n = str(number)
    set_n = set(str_n)
    if '0' in set_n or str_n[len(str_n) - 1] == '2' or str_n[len(str_n) - 1] == 5:
        return False
    if len(str_n) != len(set_n):
        return False
    if number % 6 != 1 and number % 6 != 5:
        return False
    for i in range(2, floor(sqrt(number))):
        if number % i == 0:
            return False
    else:
        return True


def smallest_good_prime(pattern):
    max_n = ''
    min_n = ''
    for i in range(len(pattern)):
        if pattern[i] == '_':
            max_n += '9'
            min_n += '0'
        else:
            max_n += pattern[i]
            min_n += pattern[i]

    if min_n[0] == '0':
        min_n = 10**(len(min_n)-1) + int(min_n)
    else:
        min_n = int(min_n)
    max_n = int(max_n)

    L = find_all_prime_under_number(max_n)
    for i in range(min_n, max_n + 1):
        if L[i]:
            flag = [True] * 11
            str_i = str(i)
            for _ in range(len(str_i)):
                if flag[int(str_i[_])]:
                    flag[int(str_i[_])] = False
                else:
                    flag[10] = False
                    break
            if '0' in str_i or (not flag[10]):
                continue
            else:
                for _ in range(len(pattern)):
                    if pattern[_] == '_':
                        continue
                    else:
                        if str_i[_] != pattern[_]:
                            break
                else:
                    return i
    else:
        return


def find_all_prime_under_number(n):
    L = [True] * (n+1)
    L[0] = L[1] = False
    for i in range(2, floor(sqrt(n)) + 1):
        if L[i]:
            for j in range(i * i, n + 1, i):
                L[j] = False
    return L
    #return [i for i in range(2, n+1) if L[i]]
    #return compress(range(n+1),L)


#print(find_all_prime_under_number(10000000))
#print(is_good_prime(4357))
# print(smallest_good_prime('2'))
#print(timeit("find_all_prime_under_number(100_000_000)", globals=globals(), number=1))
# n = '____7___'
print((find_all_prime_under_number(11)))
# print(max_n, min_n)