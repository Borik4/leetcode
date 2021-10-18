# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.

class Solution:
    def minJumps(self, arr) -> int:
        if len(arr) > 10:
            arr_1 = [arr[0], arr[1]]
            count = 0
            for i in range(2, len(arr)):
                if not arr_1[i - 2 - count] == arr_1[i - 1 - count] == arr[i]:
                    arr_1.append(arr[i])
                else:
                    count += 1
            arr = arr_1

        self.indexes = {}
        for i in range(len(arr)):
            if arr[i] not in self.indexes:
                self.indexes[arr[i]] = []
            self.indexes[arr[i]].append(i)
        self.arr = arr
        self.step = set()
        self.last_step = {0}
        self.last_elelment = len(self.arr) - 1
        self.all_steps = {0}
        count = 0
        while True:
            if self.last_elelment in self.last_step:
                return count
            count += 1
            self.next_step()

    def next_step(self):
        for i in self.last_step:
            if i + 1 < len(self.arr) and i + 1 not in self.all_steps:
                self.step.add(i + 1)
                self.all_steps.add(i + 1)
            if i - 1 >= 0 and i - 1 not in self.all_steps:
                self.step.add(i - 1)
                self.all_steps.add(i - 1)
            for p in self.indexes[self.arr[i]]:
                if self.arr[p] == self.arr[i] and p != i and p not in self.all_steps:
                    self.all_steps.add(p)
                    self.step.add(p)

        self.last_step = self.step
        self.step = set()

p = Solution()
print(p.minJumps([7,6,9,6,9,6,9,7]), '  ==   1')
print(p.minJumps([11,22,7,7,7,7,7,7,7,22,13]), '  ==   3')
print(p.minJumps([100,-23,-23,404,100,23,23,23,3,404]), '  ==   3')