import math
def is_palindrome(num):
    n = math.floor(math.log(num, 10)) + 1
    msd_mask = pow(10, n - 1)
    for i in range(n//2):
        if num//msd_mask != num%10:
            return False
        num = num%msd_mask
        num = num//10
        msd_mask = msd_mask//100
    return True


print(is_palindrome(15151))
