"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where
a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions
would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.

"""

import math


class Solution:
    def last_exec(self, n, k):
        last_exec = None
        next_exec_index = 0

        prisoners = list(range(1, n + 1))

        while prisoners:
            print("num of prisoners left is ", len(prisoners))
            next_exec_index = (next_exec_index + k - 1) % len(prisoners)
            last_exec = prisoners.pop(next_exec_index)
            # prisoners = prisoners[:next_exec_index] + prisoners[next_exec_index + 1:]
            print(prisoners)
        return last_exec


if __name__ == '__main__':
    s = Solution()
    print(s.last_exec(5, 2))