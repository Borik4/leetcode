# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num * 0.5
        return x - int(x) == False

p = Solution()
print(p.isPerfectSquare(2000105819))