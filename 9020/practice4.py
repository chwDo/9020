from math import sqrt
from random import seed, randint
from statistics import mean, median, pstdev


def median_1(List):
    List.sort()
    if nb_of_elements % 2 == 1:
        mymedian = List[nb_of_elements // 2]
    else:
        mymedian = (List[nb_of_elements // 2] + List[nb_of_elements // 2 - 1]) / 2
    return mymedian


nb_seed = int(input('Input a seed for the random number generator: '))
nb_of_elements: int = int(input('How many elements do you want to generate? '))
seed(nb_seed)
number_list = []
Sum = 0
for i in range(nb_of_elements):
    temp = randint(-50, 50)
    number_list.append(temp)
    Sum += temp
print('\nThe list is:', number_list)
mean_1 = Sum / nb_of_elements

Sum = 0
for i in number_list:
    Sum += (i - mean_1) ** 2
standard_deviation = sqrt(Sum / nb_of_elements)
print('\nThe mean is %.2f.' % mean_1)
print('The median is %.2f.' % median_1(number_list))
print('The standard deviation is %.2f.' % standard_deviation)
print('\nConfirming with functions from the statistics module:')
print('The mean is %.2f.' % mean(number_list))
print('The median is %.2f.' % median(number_list))
print('The standard deviation is %.2f.' % pstdev(number_list))
