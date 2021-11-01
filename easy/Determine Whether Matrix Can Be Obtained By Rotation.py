# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.


class Solution:
    def findRotation(self, mat, target) -> bool:

        if self.func(mat, target):
            return True

        for op in range(3):
            matrix = list()
            for i in mat:
                matrix.append(list())
            for i in range(len(matrix)):
                for p in mat:
                    matrix[i].append(p[len(p) - 1 - i])
            for i in range(len(matrix)):
                for p in range(len(matrix[i])):
                    mat[i][p] = matrix[i][p]

            if self.func(mat, target):
                return True


        return False

    def func(self, lis_1, lis_2):
        for i in range(len(lis_1)):
            for p in range(len(lis_1[i])):
                if lis_1[i][p] != lis_2[i][p]:
                    return False
        return True


p = Solution()
print(p.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))