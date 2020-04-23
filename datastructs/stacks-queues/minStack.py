class Empty(Exception):
    pass


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ms = []
        self.aux = []

    def push(self, x):
        self.ms.append(x)
        if len(self.aux) == 0:
            self.aux.append(x)
            self.m = self.aux[-1]
        elif len(self.aux) > 0 and x <= self.aux[-1]:
            self.aux.append(x)

    def pop(self):
        if len(self.ms) == 0:
            raise Empty("stack is empty")
        if self.ms[-1] == self.aux[-1]:
            self.aux = self.aux[:-1]
        self.ms = self.ms[:-1]

    def top(self):
        last = self.ms[-1]
        return last

    def getMin(self):
        return self.aux[-1]


"""
["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
[[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
"""
# Your mStack object will be instantiated and called as such:
# obj = mStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getm()


if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)

    print(s.getMin())
    # print(s.getMin())
    s.pop()
    print(s.top())
    # print(s.top())
    print(s.getMin())
    # s.pop()
    # print(s.getMin())
