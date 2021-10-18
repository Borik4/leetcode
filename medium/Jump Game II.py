# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums) -> int:
        if len(nums) == 1:
            return 0
        your_index = 0
        count = 0
        while your_index+nums[your_index] < len(nums)-1:
            num = nums[your_index]
            best = 0

            index = 0
            for i in range(1, num+1):
                index_i = i + your_index
                best_i = index_i+nums[index_i]
                if best < best_i:
                    best = best_i
                    index = index_i
            your_index = index
            count += 1
        return count+1

p = Solution()
print(p.jump([2,3,0,1,4]), '  ==  2')
print(p.jump([2,3,1,1,4]), '  ==  2')