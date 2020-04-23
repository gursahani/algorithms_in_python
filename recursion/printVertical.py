class Solution:
    def printVertically(self, s: str):
        arr = []
        strarr = s.split(" ")
        for i in range(len(strarr)):
            word = strarr[i]

            for j in range(len(word)):
                arr.append(word[j])
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.printVertically("CONTEST IS COMING"))