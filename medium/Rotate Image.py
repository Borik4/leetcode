class Solution:
    def rotate(self, matrix) -> None:
        for op in range(3):
            mat = list()
            for i in matrix:
                mat.append(list())
            for i in range(len(mat)):
                for p in matrix:
                    mat[i].append(p[len(p)-1-i])
            for i in range(len(mat)):
                print(mat[i])
                for p in range(len(mat[i])):
                    matrix[i][p] = mat[i][p]

        return matrix

p = Solution()
print(p.rotate([[1,2,3],[4,5,6],[7,8,9]]))