# There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.
#
# You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.
#
# For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
# The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.
#
# For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
# Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.
#
# Note: There will be no obstacles on points 0 and n.

class Solution:
    def minSideJumps(self, obstacles) -> int:
        self.your_line = 2
        self.your_num = 0
        self.obstacles = obstacles
        self.num_obstacle = {}
        for i in range(len(self.obstacles)):
            if self.obstacles[i] not in self.num_obstacle:
                self.num_obstacle[self.obstacles[i]] = []
            self.num_obstacle[self.obstacles[i]].append(i)
        count = 0
        for i in range(1, len(self.obstacles)):
            k = self.obstacles[i]
            # print(self.your_line, '    >    ', self.your_num)
            if self.obstacles[i] == self.your_line:
                self.left_right()
                count += 1
            self.your_num+=1
        return count

    def left_right(self):
        if self.obstacles[self.your_num] == 0:
            count = 1
            while count+self.your_num < len(self.obstacles)-1:
                count += 1
                if self.obstacles[self.your_num+count] == 1 != self.obstacles[self.your_num + 1]:
                    if self.obstacles[self.your_num+1] == 2:
                        self.your_line = 3
                        return None
                    else:
                        self.your_line = 2
                        return None
                elif self.obstacles[self.your_num+count] == 2 != self.obstacles[self.your_num + 1]:
                    if self.obstacles[self.your_num+1] == 1:
                        self.your_line = 3
                        return None
                    else:
                        self.your_line = 1
                        return None
                elif self.obstacles[self.your_num+count] == 3 != self.obstacles[self.your_num + 1]:
                    if self.obstacles[self.your_num+1] == 2:
                        self.your_line = 1
                        return None
                    else:
                        self.your_line = 2
                        return None
            if self.your_line != 2:
                self.your_line = 2
            else:
                self.your_line = 1

        else:


            if 1 != self.obstacles[self.your_num] and 1 != self.your_line:
                self.your_line = 1
            elif 2 != self.obstacles[self.your_num] and 2 != self.your_line:
                self.your_line = 2
            elif 3 != self.obstacles[self.your_num] and 3 != self.your_line:
                self.your_line = 3


p = Solution()
print(p.minSideJumps([0,1,1,3,3,0]), '  ==   0')
print(p.minSideJumps([0,1,2,3,0]), '  ==   2')