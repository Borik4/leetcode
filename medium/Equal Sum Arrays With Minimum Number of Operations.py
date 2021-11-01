# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.
#
# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
#
# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

class Solution:
    def minOperations(self, nums1, nums2) -> int:
        if len(nums1) > 6*len(nums2) or len(nums2) > 6*len(nums1):
            return -1
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        self.num = abs(sum1 - sum2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        count = 0
        if sum1 > sum2:
            count += self.count(nums1[::-1], nums2)
        elif sum1 < sum2:
            count += self.count(nums2[::-1], nums1)
        return count

    def count(self, maximum, minimum):
        count = 0
        while self.num > 0:
            count += 1
            if len(maximum) > 0:
                num_1 = maximum[0] - 1
            else:
                num_1 = -float('inf')
            if len(minimum) > 0:
                num_2 = 6 - minimum[0]
            else:
                num_2 = -float('inf')

            if num_2 > num_1:
                minimum.pop(0)
                self.num -= num_2
            else:
                maximum.pop(0)
                self.num -= num_1


        return count





p = Solution()
print(p.minOperations([6, 6], [1]))
