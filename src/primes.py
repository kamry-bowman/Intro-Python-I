

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


for i in range(1, 40):
    print(i, isPrime(i))

# still in process
# def primeFactors(num):
#     candidates = list(range(2, num))
#     for i, candidate in enumerate(candidates):
#         if candidate:
#             step = candidate
#             pointer = i + step
#             sub_candidate = candidate
#             while sub_candidate ** 2 < num:
#                 print(sub_candidate, pointer)
#                 if sub_candidate:
#                     candidates[pointer] = False
#                 pointer += step
#                 sub_candidate = candidates[pointer]
#     return [i for i in candidates if i]


# print(primeFactors(40))
