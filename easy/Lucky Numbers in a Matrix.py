# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

class Solution:
    def luckyNumbers (self, matrix):
        ret = []
        for i in range(len(matrix)):
            t = min(matrix[i])
            if matrix[i].count(t) >= 2:
                continue
            index = matrix[i].index(t)
            if t == max([matrix[p][index] for p in range(len(matrix))]) and [matrix[p][index] for p in range(len(matrix))].count(t) == 1:
                ret.append(t)
        return ret

p = Solution()
print(p.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))