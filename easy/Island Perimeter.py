# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


class Solution:
    def island(self, ai, aa, grid):
        num = 0
        if ai + 1 == len(grid):
            num += 1
        else:
            if grid[ai + 1][aa] == 0:
                num += 1
        if ai - 1 == -1:
            num += 1
        else:
            if grid[ai - 1][aa] == 0:
                num += 1
        if aa + 1 == len(grid[0]):
            num += 1
        else:
            if grid[ai][aa + 1] == 0:
                num += 1
        if aa - 1 == -1:
            num += 1
        else:
            if grid[ai][aa - 1] == 0:
                num += 1
        return num

    def islandPerimeter(self, grid) -> int:
        num = 0
        for i in range(len(grid)):
            for a in range(len(grid[i])):
                if grid[i][a] == 1:
                    num += self.island(i, a, grid)
        return num


p = Solution()
print(p.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), '  ==  16')
print(p.islandPerimeter([[1]]), '  ==  4')