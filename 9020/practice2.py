from random import seed, randint

from numpy import *

user_seed = int(input('Input a seed for the random number generator: '))
nb_of_elements = int(input('How many elements do you want to generate? '))
seed(user_seed)
user_list = [randint(0, 99) for i in range(nb_of_elements)]
print('\nThe list is:', user_list)
nb_max = 0
nb_min = 100
for i in user_list:
    if nb_max < i:
        nb_max = i
    if nb_min > i:
        nb_min = i
print('\nThe maximum difference between largest and smallest values in this list is: %d' % (nb_max - nb_min))
print('Confirming with builtin operations: %d' % (max(user_list) - min(user_list)))
