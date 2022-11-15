from math import sqrt,floor


def claims_is_not_prime(a, p):
    if not p % a:
        return True
    bits = bin(p - 1)[2:]
    one_or_p_minus_one = {1, p - 1}
    power = a
    for b in bits[1 :]:
        previous_power = power
        power = power ** 2 % p
        if power == 1 and previous_power not in one_or_p_minus_one:
            return True
        if b == '1':
            power = power * a % p
    return power != 1

    # REPLACE PASS ABOVE WITH YOUR CODE


def miller_rabin_primality_test(witnesses, p):
    return not any(claims_is_not_prime(a, p) for a in witnesses)
    # REPLACE PASS ABOVE WITH YOUR CODE


def smallest_miller_rabin_primality_test_failure(witnesses, upper_bound):
    sieve = sieve_of_primes_up_to(upper_bound)
    for i in range(max(witnesses) + 1, len(sieve)):
        if not sieve[i] and miller_rabin_primality_test(witnesses, 2 * i + 1):
            return 2 * i + 1


def sieve_of_primes_up_to(n):
    # We let primes_sieve encode the sequence
    # (2, 3, 5, 7, 9, 11, ..., n') with n' equal to n if n is odd and
    # n - 1 is n is even. The index of n' is n_index
    n_index = (n - 1) // 2
    sieve = [True] * (n_index + 1)
    for k in range(1, (round(sqrt(n)) + 1) // 2):
        if sieve[k]:
            # If k is the index of p then 2 * k * (k + 1) is the index
            # of p ** 2. Also, we increment the value by 2p, which
            # corresponds to increasing the index by 2 * k + 1.
            for i in range(2 * k * (k + 1), n_index + 1, 2 * k + 1):
                sieve[i] = False
    return sieve

def find_all_prime_under_number(n):
    L = [True] * (n+1)
    L[0] = L[1] = False
    for i in range(2, floor(sqrt(n))):
        if not L[i]:
            continue
        for j in range(i * i, n +1, i):
            L[j] = False
    return [i for i in range(2, n+1) if L[i]]
# POSSIBLY DEFINE OTHER FUNCTIONS
#print(smallest_miller_rabin_primality_test_failure((2,7), 1000000))
print(claims_is_not_prime(3,101))