# Created by Kunal Gursahani at 11-19-2019 8:51 PM
# Last updated at 11-19-2019 8:51 PM



def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one([1, 2, 9]))
print(plus_one([9, 9, 9]))