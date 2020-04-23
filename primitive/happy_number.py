import math


class Solution:
    # def isHappy(self, n: int) -> bool:
    #     size = math.floor(math.log(n, 10)) + 1
    #
    #     for i in range(size):
    #         num = n%10

    def sum_of_sq_dig(self, num):
        total = 0
        while num > 0:
            total += (num % 10) ** 2
            num = num // 10
        return total

    def is_happy(self, n):
        seen = []
        while n > 1 and n not in seen:
            seen.append(n)
            n = self.sum_of_sq_dig(n)
        return n == 1

    def fib(self):
        a = 0
        b = 1
        while True:
            yield a
            future = a + b
            a = b
            b = future

    def fib_(self, n):
        a, b = 0, 1

        for i in range(n):
            yield a
            a, b = b, a + b

    def inf_seq(self):
        a = 0
        while True:
            yield a
            a += 1


if __name__ == '__main__':
    s = Solution()
    # print(s.isHappy(195))
    # g = s.fib()
    # print(s.sum_of_sq_dig(20))
    print(s.is_happy(20))
    # print(s.is_happy(20))
