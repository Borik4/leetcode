# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        your_index = 0
        count = 0
        for i in range(len(nums)):
            if your_index + nums[your_index] >= len(nums) - 1:
                return True
            num = nums[your_index]
            best = 0

            index = 0
            for i in range(1, num + 1):
                index_i = i + your_index
                best_i = index_i + nums[index_i]
                if best < best_i:
                    best = best_i
                    index = index_i
            your_index = index
            count += 1

        return False

p = Solution()
print(p.canJump([2,3,1,1,4]), '  ==   True')
print(p.canJump([3,2,1,0,4]), '  ==   False')