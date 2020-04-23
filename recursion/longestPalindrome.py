class Solution:
    def __init__(self):
        self.hashmap = {}

    def longestPalindrome(self, s: str) -> str:
        if self.is_palindrome(s):
            self.hashmap[s] = len(s)

        # if len(s) <= 1:
        #     return len(s)
        # else:
        #     o = ""
        #     m = {}
        #     longest_length = 0
        #     # print(len(s))
        #     for i in range(len(s)):
        #         o += s[i]
        #         print(o)
        #         if self.is_palindrome(o):
        #             m[o] = len(o)
        #     # print(m)
        #     longest_pal = ""
        #     print(m.items())
        #     for j, i in m.items():
        #         # print(i)
        #         if i > longest_length:
        #             longest_length = i
        #             longest_pal = j
        #     return longest_pal

    def is_palindrome(self, o):
        if len(o) <= 1:
            return True
        else:
            left = 0
            right = len(o) - 1
            while left < right:
                if o[left] != o[right]:
                    return False
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('cbbd'))
