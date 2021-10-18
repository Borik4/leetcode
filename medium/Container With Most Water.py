# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        max_water = 0
        while i < j:
            effective_height = min(height[i], height[j])
            max_water = max(max_water, (j - i) * effective_height)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water

p = Solution()
print(p.maxArea([1,8,6,2,5,4,8,3,7]), '  ==  49')
print(p.maxArea([1,1]), '  ==  1')