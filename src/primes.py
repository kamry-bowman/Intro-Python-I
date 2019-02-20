import math
from itertools import islice


def isPrime(original_num):
    def primeHelper(num, candidate):
        if (candidate == 1):
            return True
        if (num % candidate == 0):
            return False
        else:
            return primeHelper(num, candidate - 1)

    if (original_num == 1):
        return True
    if (original_num == 2):
        return False
    return primeHelper(original_num, original_num // 2)


def int_sqrt(num):
    candidate = 1
    squared = candidate * candidate

    while squared <= num:
        candidate += 1
        squared = candidate * candidate
    return candidate - 1


# for i in range(1, 40):
#     print(i, isPrime(i))


def primes_factors(num):
    candidates = [True for i in range(num + 1)]
    p = 2

    while p <= num:
        if candidates[p]:
            if num % p == 0:
                candidates[p] = False
            for q in range(p * p, num + 1, p):
                candidates[q] = False
        p += 1

    return [i for i in range(2, num + 1) if candidates[i]]


print(primes_factors(21))
