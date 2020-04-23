class Solution:
    def sort_strings(self, str1):
        my_map = dict()
        for i in range(len(str1)):
            if str1[i] in my_map:
                my_map[str1[i]] += 1
            else:
                my_map[str1[i]] = 1
        return self.returnString(my_map)

    def returnString(self, my_map):
        # keys = my_map.values()
        output = ''
        s = sorted(my_map.items(), key=lambda item: item[1], reverse=True)
        for k, v in dict(s).items():
            output += k*v
        # print(output)
        return output




if __name__ == '__main__':
    s = Solution()
    print(s.sort_strings('tweet'))
