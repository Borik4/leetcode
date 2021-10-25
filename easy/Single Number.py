#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums) -> int:
        st = set()
        st_1 = set()
        for i in nums:
            if i not in st:
                st.add(i)
            else:
                st_1.add(i)
        return list(st.difference(st_1))[0]

p = Solution()
print(p.singleNumber([2,2,1]))