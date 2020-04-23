class Add:
    def add_lists(self, list1, list2):
        list3 = []
        carry = 0
        print(len(list1))
        print(len(list2))
        
        for i in range(3, -1, -1):
            print(i)
            sum = list1[i] + list2[i] + carry
            if sum > 9:
                carry = sum // 10
                sum = sum % 10

            else:
                carry = 0
            list3.append(sum)

        return list3


if __name__ == '__main__':
    m = Add()
    print(1234 + 678)
    print(m.add_lists([1, 2, 3, 4], [0, 6, 7, 8]))
