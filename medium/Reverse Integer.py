# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            x = int('-' + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])

        if -2147483648 <= x <= 2147483647:
            return x
        return 0

p = Solution()
print(p.reverse(123), '  ==  321')
print(p.reverse(-123), '  ==  -321')