# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for c in range(i, len(nums)):
                if nums[i] + nums[c] == target and i != c:
                    return [i, c]


p = Solution()
print(p.twoSum([2,7,11,15], 9), '  ==  [0, 1]')
print(p.twoSum([3, 2, 4], 6), '  ==  [1, 2]')
print(p.twoSum([3, 3], 6), '  ==  [0, 1]')