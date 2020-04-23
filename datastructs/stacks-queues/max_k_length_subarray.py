from collections import deque
class Solution:

    def max_of_subarrays(self, arr, k):
        output = []
        for i in range(0, len(arr) - k + 1):
            print(arr[i:i + k])
            output.append(max(arr[i:i+k]))
        return output

    def max_of_sub_q(self, arr, k):
        q = deque()
        for i in range(k):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
                q.append(i)

        for i in range(k, len(arr)):
            print(arr[q[0]])
            while q and q[0] <= i -k:
                q.popleft()
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
                q.append(i)
                print(arr[q[0]])


if __name__ == '__main__':
    s = Solution()
    print(s.max_of_subarrays([10, 5, 2, 7, 8, 7], 3))
