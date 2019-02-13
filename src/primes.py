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


for i in range(1, 40):
    print(i, isPrime(i))


def primes_factors(num):
    candidates = list(range(2, num))
    for i, candidate in enumerate(candidates):
        if candidate:
            if num % candidate == 0:
                candidates[0] = False
            step = candidate
            pointer = i + step
            while pointer < len(candidates):
                candidates[pointer] = False
                pointer += step

    return [i for i in candidates if i]


print(primes_up_to(100))
