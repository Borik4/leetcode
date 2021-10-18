# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


class Solution:
    def arrayPairSum(self, nums) -> int:
        return sum(sorted(nums)[::2])

p = Solution()
print(p.arrayPairSum([1,4,3,2]), '  ==  4')