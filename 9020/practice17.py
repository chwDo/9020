while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')
line = [0] + [0] * (2 * N + 1)+[0]
new_line = line.copy()
line[N+1] = 1
for j in range(0,N):
    for _ in line[2:-2]:
        if _ == 0:
            print('  ', end='')
        else:
            print(_, end='')
    print()
    for i in range(1, 2 * N + 1):
        new_line[i] = line[i-1]+line[i + 1]
    line = new_line.copy()

