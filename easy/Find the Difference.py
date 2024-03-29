# You are given two strings s and t.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Return the letter that was added to t.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        num_s = {}
        num_t = {}
        for i in s:
            if i not in num_s:
                num_s[i] = 0
            num_s[i] += 1
        for i in t:
            if i not in num_t:
                num_t[i] = 0
            num_t[i] += 1

        for i in num_t:
            if i in num_s:
                if num_s[i] != num_t[i]:
                    return i
            else:
                return i

p = Solution()
print(p.findTheDifference('abcd', "abcde"))