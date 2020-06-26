class Solution:
    def is_prime(self, num):
        for i in range(2, num):

            if num % i == 0:
                return False

        return True




if __name__ == '__main__':
    print(Solution().is_prime(12))
