from math import sqrt,floor

L = [0] * 1000
for i in range(0, floor(sqrt(1000))):
    for j in range(1, floor(sqrt(1000))):
        sum_of_pow2 = i**2 + j**2
        if 100 <= sum_of_pow2 <= 999 and L[sum_of_pow2] == 0:
            L[sum_of_pow2] = i, j

for i in range(100, 996):
    if L[i] != 0 and L[i+1] != 0 and L[i + 2] != 0:
        print(tuple(i + _ for _ in range(0,3)),
              f'(equal to ({L[i][0]}^2+{L[i][1]}^2, '
              f'{L[i+1][0]}^2+{L[i+1][1]}^2, '
              f'{L[i+2][0]}^2+{L[i+2][1]}^2)) is a solution.')