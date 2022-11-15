M = 6
N = 4

def dice(m, n, pos, lis):
    if n > 0:
        for i in reversed(range(n,m+1)):
            lis[pos] = chr(i+ord('0'))
            dice(i-1, n-1, pos+1, lis)
    else:
        print(''.join(lis))

dice(M, N, 0, ['0']*N)