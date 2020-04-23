class Fib:
    cache = {}

    def fib(self, n):
        if n in self.cache:
            ans = self.cache[n]

        else:
            if n < 2:
                ans = n
                self.cache[n] = ans
            else:

                ans = self.fib(n - 1) + self.fib(n - 2)
                self.cache[n] = ans
        return ans


if __name__ == '__main__':
    f = Fib()

    print(f.fib(100))