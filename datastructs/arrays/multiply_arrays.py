# Created by Kunal Gursahani at 11-19-2019 9:40 PM
# Last updated at 11-19-2019 9:40 PM


def multiply(a, b):
    # num3 = [0] * (len(num1) + len(num2))
    # for i in reversed(range(len(num1))):
    #     for j in reversed(range(len(num2))):
    #         num3[i + j] += num1[i] * num2[j]
    #         # num3[i + j] += num3[i + j + 1]
    #         num3[i + j + 1] %= 10

    c = [0] * (len(a) + len(b))  # initialize result with zeros

    for i in range(0, len(a)):  # cycle over a
        for j in range(0, len(b)):  # cycle over b
            c[i + j] += a[i] * b[j]  # elementary mul and add
    return c


print(multiply([1, 2, 3], [2, 4, 6]))
