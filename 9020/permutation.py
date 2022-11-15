def permutations_2(arr, position, end):  #递归
    if position == end:
        print(arr)

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations_2(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


def permutations_1(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))         #输出索引
    cycles = list(range(n, n-r, -1))    #共有 n*(n-1)..(n-r)种可能
    print(tuple(pool[i] for i in indices[:r]))
    while 1:
        for i in reversed(range(r)):   #从尾部开始交换
            cycles[i] -= 1              #输出一次减一
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]#将输出索引还原
                cycles[i] = n - i  #将cycles数组的尾数还原
                #不放break非常重要
            else:
                j = cycles[i]  #调换倒数第j位的数
                indices[i], indices[-j] = indices[-j], indices[i] #调换第j位的数
                print(tuple(pool[i] for i in indices[:r])) #输出
                break
        else:
            return   #所有可能遍历结束 结束

def my_permutation(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n,n-r,-1))
    yield (tuple(pool[i] for i in indices[:r]))
    while 1:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield(tuple(pool[i] for i in indices[:r]))
                break
        else:
            return


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    print(n-r)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
#print(list())
permutations_1('ABCD', r=2)
#print(list(my_permutation('1234', r=3)))
# print(list(permutations_1('SETTLEMENT')))
#permutations_2(['A','B','C','D'],0,4)

