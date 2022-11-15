def smart_computation(x):
    print(f'Computing the number of trailing 0s in {x}! the smart way...')
    nb_of_trailing_0s = 0
    power_of_five = 5
    while x >= power_of_five:
        nb_of_trailing_0s += x // power_of_five
        power_of_five *= 5
        print(nb_of_trailing_0s)
    return nb_of_trailing_0s


print(smart_computation(25))