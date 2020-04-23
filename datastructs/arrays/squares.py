# LC - 977. Squares of a Sorted Array
class Solution:

    def sortedSquares(self, a: [int]) -> [int]:

        length = len(a)
        b = [None] * len(a)
        left = 0
        right = len(a) - 1
        while left <= right:
            lvalue = a[left] * a[left]
            rvalue = a[right] * a[right]
            length -= 1
            if lvalue > rvalue:
                b[length] = lvalue
                left += 1
            else:
                b[length] = rvalue
                right -= 1

        return b

        # for i in range(len(a)):
        #     square = a[i] * a[i]
        #     if len(b) == 0:
        #         b.append(square)
        #     elif square < b[i - 1]:
        #         b.append(b[i-1])
        #         b[i-1] = square
        #     elif square > b[i - 1]:
        #         b.append(square)



if __name__ == '__main__':
    s = Solution()
    x = s.sortedSquares([-4, -1, 0, 3, 10])
    print(x)
