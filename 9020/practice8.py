def balanced_brackets_in(pattern):
    if pattern == ' ':
        return True
    l = ' ()[]{}'
    flag = True
    for i in pattern:
        if i not in l:
            flag = False
            break
    if flag:
        return judge(pattern)
    return None


def judge(pattern):
    pattern = list(pattern)
    dir_bracket = {')': '(', '}': '{', ']': '['}
    close_brackets = ')}]'
    for i, j in enumerate(pattern):
        if j == ' ':
            continue
        if j in close_brackets:
            index = last_open_brackt(i-1, pattern)
            if index == -1:
                return False
            if dir_bracket[j] != pattern[index]:
                return False
            else:
                pattern[index] = '#'
                pattern[i] = '#'
            #print(pattern)
    for _ in pattern:
        if _ != '#':
            return False
    return True

def last_open_brackt(i, pattern):
    open_bracket = ['[', '{', '(']
    for index, _ in enumerate(pattern[i::-1]):
        if _ in open_bracket:
            #print(i-index)
            return i - index
    return -1


# for index, _ in enumerate(pattern[3::-1]):
#     print(index, _)
print(balanced_brackets_in(" ("))
# Written by Eric Martin for COMP9021
#
#
# def balanced_brackets_in(pattern):
#     pattern = iter(pattern)
#     for symbol in pattern:
#         if not symbol.isspace():
#             break
#     else:
#         return True
#     brackets = dict(zip('([{', ')]}'))
#     if symbol not in brackets:
#         for bracket in brackets:
#             if symbol == brackets[bracket]:
#                 return extra_symbols_or_imbalanced(pattern,
#                                                    (bracket, brackets[bracket])
#                                                   )
#         return
#     nb_of_opening_brackets = 1
#     for c in pattern:
#         if c == symbol:
#             nb_of_opening_brackets += 1
#         elif c == brackets[symbol]:
#             if not nb_of_opening_brackets:
#                 return extra_symbols_or_imbalanced(pattern,
#                                                    (symbol, brackets[symbol])
#                                                   )
#             nb_of_opening_brackets -= 1
#         elif not c.isspace():
#             return
#     return not nb_of_opening_brackets
#
# def extra_symbols_or_imbalanced(pattern, brackets):
#     if all(c.isspace() or c in brackets for c in pattern):
#         return False
#     return
# print(balanced_brackets_in(" ( "))