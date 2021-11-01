# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
from copy import deepcopy

class Solution:
    def permute(self, nums):
        self.lis = [[]]
        self.last_lis = []
        self.recurs(nums)
        return self.lis
    def recurs(self, nums):
        print(len(self.lis[0]), len(nums))
        while len(self.lis[0]) != len(nums):
            for i in self.lis:
                for p in nums:
                    if p not in i:
                        w = deepcopy(i)
                        w.append(p)
                        self.last_lis.append(w)

            self.lis = self.last_lis
            self.last_lis = []
            print(self.lis)


        return self.lis

p = Solution()
print(p.permute([1,2,3,4]))
