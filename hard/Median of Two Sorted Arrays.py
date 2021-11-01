# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        list = sorted(nums1 + nums2)
        if not len(list) % 2:
            return (list[len(list) // 2] + list[len(list) // 2-1]) / 2
        return list[len(list) // 2]
p = Solution()
print(p.findMedianSortedArrays([1,2], [3,4]))