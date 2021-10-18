# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.


class Solution:
    def dayOfYear(self, date: str) -> int:
        lis = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = date[0:4]
        month = date[5:7]
        day = date[8::]
        if int(year) % 4 == 0 and int(month) > 2:
            return sum(lis[0:int(month)-1]) + int(day) + 1
        return sum(lis[0:int(month)-1]) + int(day)


p = Solution()
print(p.dayOfYear("2019-02-10"), '  ==  41')
print(p.dayOfYear("2003-03-01"), '  ==  60')