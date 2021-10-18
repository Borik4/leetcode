# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#
# Notice that you can not jump outside of the array at any time.

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.c = {}
        for i in range(len(arr)):
            self.c[i] = set()
        for i in range(len(arr)):
            if 0 <= i-arr[i] < len(arr):
                self.c[i-arr[i]].add(i)
            if 0 <= i+arr[i] < len(arr):
                self.c[i+arr[i]].add(i)
        self.arr = arr
        self.l = set()
        self.my_indexes = set()
        self.all_indexes = set()


        for i in range(len(arr)):
            if arr[i] == 0:
                self.my_indexes.add(i)
                self.all_indexes.add(i)


        while True:
            self.search()
            if start in self.all_indexes:
                return True
            if len(self.my_indexes) == 0:
                return False



    def search(self):
        for i in self.my_indexes:
            for p in self.c[i]:
                if p not in self.all_indexes:
                    self.l.add(p)
                    self.all_indexes.add(p)




        self.my_indexes = self.l
        self.l = set()



p = Solution()
print(p.canReach([4,2,3,0,3,1,2], 0), '  ==   True')
print(p.canReach([3,0,2,1,2], 2), '  ==   False')