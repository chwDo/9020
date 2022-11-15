def bwtencode():
    global L, F
    L = ''
    F = ''
    text = "12345678#"
    last_str = text
    len_text = len(text)
    rotate_list = []
    rotate_list.append(last_str)
    for i in range(len_text - 1):
        last_str = last_str[-1] + last_str[-len_text:-1]
        rotate_list.append(last_str)

    sorted_list = sorted(rotate_list)
    for eachstr in sorted_list:
        L = L + eachstr[-1]
        F = F + eachstr[0]
    print(L)


def C(c):
    # 统计T中字典序小于“c”的所有字符个数
    global L

    num_Tc = 0
    for eachchr in L:
        if c > eachchr:
            num_Tc += 1
    return num_Tc - 1


def Occ(c, r):
    # 统计L中第r行之前出现字符c的数量
    global L
    row = -1
    num_Lc = 0
    if r == 0:
        return 0
    for eachchr in L:
        row += 1
        if eachchr == c:
            num_Lc += 1
        if row == r - 1:
            break
    return num_Lc


def bwtdecode():
    # 因为#的存在，就能确定原文中的最后一个字符肯定在L的首行（首字符）
    global L
    r = 0
    T = ''

    while L[r] != "#":
        T = L[r] + T
        c = L[r]
        r = C(c) + Occ(c, r) + 1
    print(T)


bwtencode()
bwtdecode()
