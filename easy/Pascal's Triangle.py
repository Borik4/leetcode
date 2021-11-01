# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int):
        l = []
        for i in range(2, numRows+1):
            l.append([])
            for j in range(i):
                if j == 0:
                    l[-1].append(1)
                elif j == i-1:
                    l[-1].append(1)
                else:
                    l[-1].append(l[-2][j-1] + l[-2][j])
            # del l[0]
        return l

p = Solution()
print(p.generate(5))