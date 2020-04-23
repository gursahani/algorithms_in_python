class minChange:
    stack = []
    def makeChange(self, string):
        for i in range(len(string)):
            if string[i] not in self.stack:
                self.stack.append(string[i])
            else:
                temp = string[i]
                string[i] = string[i - 1]
                string[i - 1] = temp
                self.stack.append(string[i]+"insertion")
        return string


if __name__ == '__main__':
    minChange() m

