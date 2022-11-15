min_i = 10
max_i = 76
max_j = 87
max_k = 98

for i in range(min_i,max_i):
    i_digits = {i//10,i % 10}
    if len(i_digits) != 2:
        continue
    for j in range(i+1, max_j+1):
        i_and_j_digits = i_digits.union((j//10, j % 10))
        if len(i_and_j_digits) != 4:
            continue
        for k in range(j+1, max_k):
            i_j_k_digits = i_and_j_digits.union((k//10, k % 10))
            if len(i_j_k_digits) != 6:
                continue
            product = i * j * k
            product_digits = set((int(i)) for i in str(product))
            if product_digits != i_j_k_digits:
                continue
            else:
                print(f'{i} x {j} x {k} = {product} is a solution.')