from random import randint, seed


def play():
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    dic_reverse = {}
    for _ in dic:
        dic_reverse[dic[_]] = _
    keep_dice = []
    counter = 0
    while counter <= 2:
        print('The roll is: ', end='')
        L = []
        flag = [0] * 6
        if keep_dice == [] or keep_dice == ['']:
            for _ in range(5):
                n = randint(0, 5)
                flag[n] += 1
                L.append(n)
        else:
            for _ in keep_dice:
                n = dic_reverse[_]
                flag[n] += 1
                L.append(n)
            for _ in range(5 - len(keep_dice)):
                n = randint(0, 5)
                flag[n] += 1
                L.append(n)

        S = set()
        print_l = []
        for _, n in enumerate(flag):
            for __ in range(n):
                S.add(dic[_])
                print_l.append(dic[_])
        print(' '.join(print_l))

        dif = len(L) - len(S)
        maxx = 0
        for _ in flag:
            if _ > maxx:
                maxx = _
        if dif == 0:
            print('It is a Bust')
        elif dif == 1:
            print('It is a One pair')
        elif dif == 2:
            if maxx == 2:
                print('It is a Two pair')
            else:
                print('It is a Three of a kind')
        elif dif == 3:
            if maxx == 3:
                print('It is a Full house')
            else:
                print('It is a Four of a kind')
        else:
            print('It is a Five of a kind')

        f = False
        while not f and counter < 2:
            flag1 = flag.copy()
            if counter == 0:
                keep_dice = input('Which dice do you want to keep for the second roll? ').split(' ')
            else:
                keep_dice = input('Which dice do you want to keep for the third roll? ').split(' ')
            if keep_dice == ['all'] or keep_dice == ['All']:
                print('Ok, done.')
                return
            if keep_dice == ['']:
                break
            if keep_dice:
                for i in keep_dice:
                    if i not in dic_reverse:
                        print('That is not possible, try again!')
                        break
                    else:
                        flag1[dic_reverse[i]] -= 1
                        if flag1[dic_reverse[i]] < 0:
                            print('That is not possible, try again!')
                            break
                else:
                    s = sum(i for i in flag1)
                    if s == 0:
                        print('Ok, done.')
                        return
                    f = True
        counter += 1


def simulate(n):
    p_dic = {0: 'Five of a kind',
           1: 'Four of a kind',
           2: 'Full house',
           3: 'Straight',
           4: 'Three of a kind',
           5: 'Two pair',
           6: 'One pair'}
    dic = {0: 'Ace', 1: 'King', 2: 'Queen', 3: 'Jack', 4: '10', 5: '9'}
    dic_reverse = {}
    for _ in dic:
        dic_reverse[dic[_]] = _
    probability_of_patterns = [0] * 7
    nn = n
    while n > 0:
        flag = [0] * 6
        L = []
        for _ in range(5):
            number = randint(0, 5)
            flag[number] += 1
            L.append(number)
        S = set()
        for _, number in enumerate(flag):
            for __ in range(number):
                S.add(dic[_])

        dif = len(L) - len(S)
        maxx = 0
        for _ in flag:
            if _ > maxx:
                maxx = _
        if dif == 0:
            if flag[0] == 0 or flag[5] == 0:
                probability_of_patterns[3] += 1
        elif dif == 1:
            probability_of_patterns[6] += 1
        elif dif == 2:
            if maxx == 2:
                probability_of_patterns[5] += 1
            else:
                probability_of_patterns[4] += 1
        elif dif == 3:
            if maxx == 3:
                probability_of_patterns[2] += 1
            else:
                probability_of_patterns[1] += 1
        else:
            probability_of_patterns[0] += 1
        n -= 1
    for _ in range(7):
        print(f'{p_dic[_]:15}'+f': {probability_of_patterns[_] / nn * 100:.2f}%')


# DEFINE OTHER FUNCTIONS

#play()
seed(0)
simulate(1000)