# Given two integer arrays startTime and endTime and given an integer queryTime.
#
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if endTime[i] >= queryTime >= startTime[i]:
                count += 1
        return count

p = Solution()
print(p.busyStudent([1,2,3], [3,2,7], 4))