class SunsetView:

    def findSunsetView(self, stack):
        output = []
        while len(stack) > 0:
            east = stack.pop()
            if len(output) > 0 and east > output[-1]:
                output.pop()
            output.append(east)

        return list(reversed(output))


if __name__ == '__main__':
    stack = [3, 2, 1]
    sunsetView = SunsetView()
    print(sunsetView.findSunsetView(stack))
    print(sunsetView.findSunsetView([2, 5, 7]))
    print(sunsetView.findSunsetView([2, 3, 1, 4]))
