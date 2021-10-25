class Solution:
    def maxSubArray(self, nums) -> int:
        maximum = nums[-1]
        count = 0
        for i in nums:
            count += i
            maximum = max(maximum, count)
            if count < 0:
                count = 0
        return maximum

p = Solution()
print(p.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))