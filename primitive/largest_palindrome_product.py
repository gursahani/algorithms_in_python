"""A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

import math


def is_palindrome(num):
    n = math.floor(math.log(num, 10)) + 1
    msd_mask = pow(10, n - 1)
    for i in range(n // 2):
        if num // msd_mask != num % 10:
            return False
        num = num % msd_mask
        num = num // 10
        msd_mask = msd_mask // 100
    return True


def find_largest_palindrome(num1, num2):
    palindrome = 0

    for j in range(num1, num2):
        for k in range(num1+1, num2):
            prod = j * k
            # print(prod)
            if is_palindrome(prod):
                if prod > palindrome:
                    palindrome = prod

    return palindrome


print(find_largest_palindrome(100, 1000))
