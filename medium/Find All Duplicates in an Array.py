# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

class Solution:
    def findDuplicates(self, nums):
        first = set()
        res = []

        for num in nums:
            if num in first:
                res.append(num)
            else:
                first.add(num)
        return res

p = Solution()
print(p.findDuplicates([4,3,2,7,8,2,3,1]), '  ==   [2, 3]')
print(p.findDuplicates([1,1,2]), '  ==   [1]')