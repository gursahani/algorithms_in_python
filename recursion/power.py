def power(base, exp):
    ans = 1
    for i in range(exp):
        ans *= base
    return ans


def rec_power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * rec_power(base, exp - 1)


print(power(2, 4))
print(rec_power(2, 4))