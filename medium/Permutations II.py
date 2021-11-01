# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


from copy import deepcopy
class Solution:
    def permuteUnique(self, nums):
        self.lis = [[]]
        self.last_lis = []
        self.num_count = {}
        self.nums = nums
        for i in self.nums:
            if i not in self.num_count:
                self.num_count[i] = 0
            self.num_count[i] += 1
        self.recurs()
        return self.lis
    def recurs(self):
        while len(self.lis[0]) != len(self.nums):
            for i in self.lis:
                for p in self.num_count:
                    if i.count(p) < self.num_count[p]:
                        w = deepcopy(i)
                        w.append(p)
                        self.last_lis.append(w)
            self.lis = self.last_lis
            self.last_lis = []





p = Solution()
print(p.permuteUnique([1,1,2]))