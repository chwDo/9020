from random import seed, randrange

nb_seed = int(input("Input a seed for the random number generator: "))
nb_of_elements = int(input('How many elements do you want to generate? '))
seed(nb_seed)
List = [0] * 4
number_list = []
for i in range(nb_of_elements):
    number = randrange(0, 20)
    number_list.append(number)
    List[number // 5] += 1
print('\nThe list is:', number_list, '\n')
j = 0
for i in List:
    str_1 = 'no'
    if i == 0:
        print('There is %s element between %d and %d.' % (str_1, j, j + 4))
    elif i == 1:
        str_1 = str(i)
        print('There is %s element between %d and %d.' % (str_1, j, j + 4))
    else:
        str_1 = str(i)
        print('There are %s elements between %d and %d.' % (str_1, j, j + 4))
    j += 5
