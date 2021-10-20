# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.




class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        for i in strs:
            sort_i = self.sort(i)
            if sort_i not in my_dict:
                my_dict[sort_i] = []
            my_dict[sort_i].append(i)
        return list(my_dict.values())
    def sort(self, i):
        i = list(i)
        i = [ord(j) for j in i]
        i = sorted(i)
        return ''.join([chr(j) for j in i])

p = Solution()
print(p.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))





