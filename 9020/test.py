# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from math import sqrt
from itertools import permutations
from collections import Counter


# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 10_000_000.
def is_good_prime(number):
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        number_str = str(number)
        account = Counter(number_str)
        for key in account.keys():
            if key == '0':
                return False
        for value in account.values():
            if value > 1:
                return False
        return True
    return False
    # REPLACE PASS ABOVE WITH YOUR CODE


# pattern is expected to be a nonempty string consisting of underscores
# and digits of length at most 7.
# Underscores have to be replaced by digits so that the resulting number
# is the smallest good prime, in case it exists.
# The function returns that number if it exists, None otherwise.
def smallest_good_prime(pattern):
    pattern_str = str(pattern)
    while '_' not in pattern_str:
        number = pattern
        if is_good_prime(number):
            return number
        else:
            return None

    pattern_real = pattern_str.replace('_', '')
    if pattern_real != '':
        pattern_real = int(pattern_real)

    if is_good_prime(pattern_real) or pattern_real == '':
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        same_number = set(pattern_real) & set(lst)
        use_n = list(set(lst) - same_number)
        total = Counter(pattern_str)
        run_time = total['_']
        ls = permutations(use_n, run_time)
        for j in ls:
            if is_good_prime(give_new_to_empty(j, pattern)):
                return give_new_to_empty(j, pattern)
    else:
        return None
    # REPLACE PASS ABOVE WITH YOUR CODE


def give_new_to_empty(j, pattern):
    pattern_lst = list(pattern)
    j_order = 0
    l = len(pattern_lst)
    for empty in range(0, l):
        if pattern_lst[empty] == '_':
            pattern_lst[empty] = j[j_order]
            j_order = j_order + 1
    the_truth = int(pattern_lst)
    return the_truth


# POSSIBLY DEFINE OTHER FUNCTIONS
print(smallest_good_prime('__'))