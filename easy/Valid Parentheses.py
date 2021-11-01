# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s):
        self.my_dict = {'(': ')', '[': ']', '{': '}', }
        self.my_dict_2 = {')': '(', '}': '{', ']': '['}
        num_1 = 0
        num_2 = 0
        num_3 = 0
        last = []
        for i in s:
            if i in self.my_dict:
                last.append(i)
            else:
                if not len(last) or self.my_dict[last.pop()] != i:
                    return False
        if len(last) == 0:
            return True
        return False

p = Solution()

print(p.isValid('}])()}'))