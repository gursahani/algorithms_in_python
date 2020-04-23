class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6':
                return int(num[:i] + '9' + num[i + 1:])
        else:
            return int(num)


if __name__ == '__main__':
    s = Solution()
    print(s.maximum69Number(9669))
