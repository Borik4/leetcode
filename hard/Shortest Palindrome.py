# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):
            if s[0:i] == s[0:i][::-1]:
                return s[i::][::-1] + s[0:i] + s[i::]

p = Solution()
print(p.shortestPalindrome('aacecaaa'), '  ==   aaacecaaa')
print(p.shortestPalindrome("abcd"), '  ==   dcbabcd')