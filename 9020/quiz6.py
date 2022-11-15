import sys
from random import seed, randint
from collections import defaultdict
from functools import lru_cache


def display_grid():
    for row in grid:
        print(' '.join(f'{e:{len(str(upper_bound))}}' for e in row))


# @lru_cache
# def find_path(i, j):
#     directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
#     flag = 0
#     if len_grid[i][j] == 0:
#         for d in directions:
#             if i - d[0] < 0 or i - d[0] > (dim - 1) or j - d[1] < 0 or j - d[1] > (dim - 1):
#                 flag += 1
#                 continue
#             else:
#                 if grid[i - d[0]][j - d[1]] - grid[i][j] == 1:
#                     if len_grid[i - d[0]][j - d[1]] == 0:
#                         find_path(i - d[0], j - d[1])
#                     len = len_grid[i - d[0]][j - d[1]] + 1
#                     if len_grid[i][j] < len:
#                         len_grid[i][j] = len
#                 else:
#                     flag += 1
#         if flag == 4:
#             len_grid[i][j] = 1
max = [0, 0]
def find_path(i, j):
    if max[0] < grid[i][j]:
        max[0], max[1] = grid[i][j], 1
    elif max[0] == grid[i][j]:
        max[1] += 1
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for d in directions:
        if i - d[0] < 0 or i - d[0] > (dim - 1) or j - d[1] < 0 or j - d[1] > (dim - 1):
            continue
        else:
            if grid[i - d[0]][j - d[1]] - grid[i][j] == 1:
                find_path(i - d[0], j - d[1])


def value_and_number_of_longest_paths():
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == 0:
                find_path(i, j)
    return max[0], max[1]


# POSSIBLY DEFINE OTHER FUNCTIONS


provided_input = input('Enter three integers: ').split()
if len(provided_input) != 3:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    for_seed, dim, upper_bound = (abs(int(e)) for e in provided_input)  # abs()取绝对值
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randint(0, upper_bound) for _ in range(dim)] for _ in range(dim)]
len_grid = [[0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
max_value, nb_of_paths_of_max_value = value_and_number_of_longest_paths()
if not nb_of_paths_of_max_value:
    print('There is no 0 in the grid.')
else:
    print('The longest paths made up of consecutive numbers starting '
          f'from 0 go up to {max_value}.'
          )
    if nb_of_paths_of_max_value == 1:
        print('There is one such path.')
    else:
        print('There are', nb_of_paths_of_max_value, 'such paths.')
