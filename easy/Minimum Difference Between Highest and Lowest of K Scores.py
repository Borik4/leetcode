# represents the score of the ith student. You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
#
# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        d = []
        for i in range(len(nums)-k+1):
            o = nums[i+k-1] - nums[i]
            d.append(nums[i+k-1] - nums[i])
        return min(d)

p = Solution()
print(p.minimumDifference([90], 1))