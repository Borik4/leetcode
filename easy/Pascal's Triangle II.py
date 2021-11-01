# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int):
        l = [[1]]
        for i in range(2, rowIndex+2):
            l.append([])
            for j in range(i):
                if j == 0:
                    l[-1].append(1)
                elif j == i-1:
                    l[-1].append(1)
                else:
                    l[-1].append(l[-2][j-1] + l[-2][j])
            del l[0]
        return l[0]

p = Solution()
print(p.getRow(3))


