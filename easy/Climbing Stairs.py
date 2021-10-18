# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        p = 1
        pp = 1
        for i in range(2, n + 1):
            res = p + pp
            pp = p
            p = res
        return res

p = Solution()
print(p.climbStairs(2), '  ==  2')