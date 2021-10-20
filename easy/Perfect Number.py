# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
#
# Given an integer n, return true if n is a perfect number, otherwise return false.

import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        summary = 0
        for i in range(1, int(math.sqrt(num)+1)):
            if num%i == 0:
                print(i, num//i)
                summary += i+num//i
            print(summary)
        print(summary, num*2)
        return summary == num*2

p = Solution()
print(p.checkPerfectNumber(1))