# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = set(nums)
        num = 1
        while True:
            if num not in nums:
                return num
            num += 1

p = Solution()
print(p.firstMissingPositive([1,2,0]), '  ==   3')
print(p.firstMissingPositive([3,4,-1,1]), '  ==   2')