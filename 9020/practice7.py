
for x in range(100, 1_000):
    for y in range(10, 100):
        flag = True
        result_1 = x * (y % 10)
        result_2 = x * (y // 10)
        if result_1 < 1_000:
            continue
        if result_2 > 1_000:
            continue
        if result_1 + result_2 > 9_999:
            continue
        str_x = '0' + str(x)
        str_y = '0' + '0' + str(y)
        str_r_1 = str(result_1)
        str_r_2 = str(result_2) + '0'
        sum = result_1 + 10 * result_2
        str_sum = str(sum)
        c_sum = int(str_x[0]) + int(str_y[0]) + int(str_r_1[0]) + int(str_r_2[0]) + int(str_sum[0])
        for i in range(1, 4):
            if int(str_x[i]) + int(str_y[i]) + int(str_r_1[i]) + int(str_r_2[i]) + int(str_sum[i]) != c_sum:
                flag = False
                break
        if flag:
            print()
            print(f'A solution with all columns adding up to {c_sum}:')
            print('      ', ' '.join(c for c in str(x)))
            print('    ', 'x  ', ' '.join(c for c in str(y)))
            print('     -------')
            print('    ', ' '.join(c for c in str(result_1)))
            print('      ', ' '.join(c for c in str(result_2)))
            print('     -------')
            print('    ', ' '.join(c for c in str(sum)))

