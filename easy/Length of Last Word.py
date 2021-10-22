# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip()
        # return s[::-1].index(' ') if ' ' in s else len(s)
        return len(s.split()[-1])
p = Solution()
print(p.lengthOfLastWord(' a  '))