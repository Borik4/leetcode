# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

class Solution:
    def addToArrayForm(self, num, k: int):
        return [i for i in str(int(''.join([str(i) for i in num])) + k)]

p = Solution()
print(p.addToArrayForm([1,2,0,0], 34))