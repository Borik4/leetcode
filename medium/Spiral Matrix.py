# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        matrix = self.gr(matrix)
        lis = [matrix[1][1]]
        u = 1
        index = (1, 1)
        print(matrix)
        while True:
            matrix[index[0]][index[1]] = '0'
            if u == 1:
                if matrix[index[0]][index[1]+1] != '0':
                    lis.append(matrix[index[0]][index[1]+1])
                    index = (index[0], index[1]+1)
                else:
                    u += 1
                    if matrix[index[0]+1][index[1]] != '0':
                        lis.append(matrix[index[0]+1][index[1]])
                        index = (index[0]+1, index[1])
                    else:
                        break
            elif u == 2:
                if matrix[index[0]+1][index[1]] != '0':
                    lis.append(matrix[index[0]+1][index[1]])
                    index = (index[0]+1, index[1])
                else:
                    u += 1
                    if matrix[index[0]][index[1]-1] != '0':
                        lis.append(matrix[index[0]][index[1]-1])
                        index = (index[0], index[1]-1)
                    else:
                        break
            elif u == 3:
                if matrix[index[0]][index[1]-1] != '0':
                    lis.append(matrix[index[0]][index[1]-1])
                    index = (index[0], index[1]-1)
                else:
                    u += 1
                    if matrix[index[0]-1][index[1]] != '0':
                        lis.append(matrix[index[0]-1][index[1]])
                        index = (index[0]-1, index[1])
                    else:
                        break
            else:
                if matrix[index[0]-1][index[1]] != '0':
                    lis.append(matrix[index[0]-1][index[1]])
                    index = (index[0]-1, index[1])
                else:
                    u = 1
                    if matrix[index[0]][index[1]+1] != '0':
                        lis.append(matrix[index[0]][index[1]+1])
                        index = (index[0], index[1]+1)
                    else:
                        break

        return lis

    def gr(self, grid):
        gre = []
        lis = ['0' for i in range(len(grid[0]) + 2)]
        gre.append(lis)
        for i in grid:
            gre.append(['0'] + i + ['0'])
        gre.append(lis)
        return gre


p = Solution()
print(p.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))