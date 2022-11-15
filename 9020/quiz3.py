from random import seed, randrange
import functools
from collections import Counter


def give_values_to_letters(for_seed):
    seed(for_seed)
    global d
    fin = open('dictionary.txt', 'rt')
    d = set([i.strip('\n') for i in fin.readlines()])
    fin.close()
    return [randrange(1, 10) for _ in range(26)]


# word and letters are both meant to be strings of nothing but
# uppercase letters, values, a list returned by
# give_values_to_letters(). Returns:
# - -1 if word is not in dictionary.txt
# - 0 if word is in dictionary.txt but cannot be built from letters
# - the value of word according to values otherwise.
def can_be_built_from_with_value(word, letters, values):
    if word not in d:
        return -1
    L = [0] * 26
    for _ in letters:
        L[ord(_) - 65] += 1  # ord('A') == 65
    sum = 0
    for _ in word:
        L[ord(_) - 65] -= 1
        if L[ord(_) - 65] < 0:
            return 0
        sum += values[ord(_) - 65]
    return sum
    # REPLACE PASS ABOVE WITH YOUR CODE


# letters is meant to be a string of nothing but uppercase letters.
# Returns the list of words in dictionary.txt that can be built
# from letters and whose value according to values is maximal.
# Longer words come before shorter words.
# For a given length, words are lexicographically ordered.
def cmp(a, b):
    if len(a) == len(b):
        for i, j in zip(a, b):
            if ord(i) != ord(j):
                return ord(i) - ord(j)
    return len(b) - len(a)


def most_valuable_solutions(letters, values):
    L = [0] * 26
    max_sum = 0
    answer_list = []
    for _ in letters:
        L[ord(_) - 65] += 1
    for word in d:
        sum = 0
        temp_L = L.copy()
        flag = True
        for _ in word:
            temp_L[ord(_) - 65] -= 1
            if temp_L[ord(_) - 65] < 0:
                flag = False
                break
            sum += values[ord(_) - 65]
        if flag:
            if sum < max_sum:
                continue
            elif max_sum == sum:
                answer_list.append(word)
            else:
                max_sum = sum
                answer_list.clear()
                answer_list.append(word)
    answer_list.append('TAROATS')
    answer_list.sort(key=len)
    print(answer_list)
    return sorted(answer_list, key=functools.cmp_to_key(cmp))

values = give_values_to_letters(0)
print(can_be_built_from_with_value('INDOEUROPEAN', 'EPEUDOINORNA EPEUDOINORNA', values))
print(most_valuable_solutions('THISORTHATT', values))