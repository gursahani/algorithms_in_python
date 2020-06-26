"""
Given a 2x4 array like [[1 4 3 2],[5 7 8 6]], you can do three operations on it,
a. Rotate the center elements clockwise
b. Rightshift all the elements
c. swap rows
Write code to achieve a desired array eg: [[1 2 3 4][5 6 7 8]]

1 4 3 2
5 7 8 6

change to

1 2 3 4
5 6 7 8


2 1 4 3
6 5 7 8


3 2 1 4
8 6 5 7
"""



class Solution:
    def matrixoperations(self, mat):
        while mat[0] != sorted(mat[0]) and mat[1] != sorted(mat[1]):
            self.rotate_center(mat)
            self.right_shift(mat)
            self.swap_rows(mat)



    def rotate_center(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp = mat[i][i+1]
                temp2 = mat[i][i+2]
                temp3 = mat[j][j]
                temp4 = mat[j][j+2]

                print(temp, temp2 ,temp3, temp4)




if __name__ == '__main__':
    s = Solution()
    s.rotate_center([[1, 4, 3, 2],[5, 7, 8, 6]])