from functools import lru_cache
import math
arr = []


def find_prime_factors(num, arr):
    for i in range(2, num):
        if num % i == 0:
            if i not in arr:
                arr.append(i)

def is_prime(num):
    for i in range(2, num):

        if num % i == 0:
            return False

    return True


# @lru_cache(maxsize=60085147514000)
def find_largest():
    for i in range(2, math.ceil(math.sqrt(600851475143))):
        if 600851475143 % i == 0:
            if is_prime(i):
                arr.append(i)

find_largest()
print(arr)
