# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution:
    def solve(self, board) -> None:
        self.board = board
        if len(board) == 1:
            return 'p'
        self.st = {}
        for i in range(1, len(board)-1):
            for p in range(1, len(board[i])-1):
                if board[i][p] == 'O':
                    self.st[(i, p)] = 1
        self.lis = [(0, i) for i in range(len(board[0])) if board[0][i] == 'O'] + [(len(board)-1, i) for i in range(len(board[-1])) if board[-1][i] == 'O'] + [(i, 0) for i in range(len(board)) if board[i][0] == 'O'] + [(i, len(board[0])-1) for i in range(len(board)) if board[i][len(board[0])-1] == 'O']
        self.deleter()
        for x, y in self.st:
            board[x][y] = 'X'
        return board


    def deleter(self):
        istrue = True
        lis = []
        while istrue:
            istrue = False
            for x, y in self.lis:
                if (x+1, y) in self.st:
                    istrue = True
                    lis.append((x+1, y))
                    self.st.pop((x+1, y))
                if (x-1, y) in self.st:
                    istrue = True
                    lis.append((x-1, y))
                    self.st.pop((x-1, y))
                if (x, y-1) in self.st:
                    istrue = True
                    lis.append((x, y-1))
                    self.st.pop((x, y-1))
                if (x, y+1) in self.st:
                    istrue = True
                    lis.append((x, y+1))
                    self.st.pop((x, y+1))
            self.lis = self.lis + lis


p = Solution()
print(p.solve([["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]))
