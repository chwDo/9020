# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 6
# whose length is chosen by the user, displays the list,
# outputs the difference between last and first values,
# then displays the values as horizontal bars of stars,
# then displays the values as vertical bars of stars
# surrounded by a frame.


import sys
from random import seed, randrange

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                              ).split()
                        )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 7) for _ in range(length)]
print('Here are the generated values:', values)
# INSERT CODE HERE
print('\nThe difference between last and first values is:')
print('  ', values[- 1] - values[0])
print('\nHere are the values represented as horizontal bars:\n')
for i in values:
    print('    ', end='')
    for _ in range(i):
        print(' * ', end='')
    print()

# INSERT CODE HERE
print('\nHere are the values represented as vertical bars, '
      'with a surrounding frame:\n'
      )
print('  ', '-' * (3 * len(values) + 2))
max = max(values)
while max > 0:
    print('   |', end='')
    for i in values:
        if i >= max:
            print(' * ', end='')
        else:
            print('   ', end='')
    print('|')
    max -= 1

print('  ', '-' * (3 * len(values) + 2))
print()
# INSERT CODE HERE
