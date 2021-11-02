# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#

class Solution:
    def generateMatrix(self, n: int):
        matrix = self.gr(n)
        u = 1
        index = [1, 1]
        num = 1
        while True:
            matrix[index[0]][index[1]] = num
            num += 1
            if u == 1:
                if matrix[index[0]][index[1]+1] is None:
                    index[1] += 1
                else:
                    u += 1
                    if matrix[index[0]+1][index[1]] is None:
                        index[0] += 1
                    else:
                        break
            elif u == 2:
                if matrix[index[0]+1][index[1]] is None:
                    index[0] += 1
                else:
                    u += 1
                    if matrix[index[0]][index[1]-1] is None:
                        index[1] -= 1
                    else:
                        break
            elif u == 3:
                if matrix[index[0]][index[1]-1] is None:
                    index[1] -= 1
                else:
                    u += 1
                    if matrix[index[0]-1][index[1]] is None:
                        index[0] -= 1
                    else:
                        break
            else:
                if matrix[index[0]-1][index[1]] is None:
                    index[0] -= 1
                else:
                    u = 1
                    if matrix[index[0]][index[1]+1] is None:
                        index[1] += 1
                    else:
                        break
        mat = []
        for i in range(1, len(matrix)-1):
            mat.append(matrix[i][1:-1])

        return mat



    def gr(self, n):
        p = [0 for i in range(n+2)]
        li = [p]
        for i in range(n):
            li.append([0]+[None for i in range(n)]+[0])
        li.append(p)
        return li

p = Solution()
print(p.generateMatrix(20))