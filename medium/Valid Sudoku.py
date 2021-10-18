# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in board:
            st = set()
            for j in i:
                if j not in st and j != '.':
                    st.add(j)
                elif j != '.':
                    return False

        for i in range(len(board)):
            st = set()
            for j in range(len(board)):
                if board[j][i] not in st and board[j][i] != '.':
                    st.add(board[j][i])
                elif board[j][i] != '.':
                    return False
        for i in range(3):
            for k in range(3):
                st = set()
                if board[i*3][k*3] not in st and board[i*3][k*3] != '.':
                    st.add(board[i*3][k*3])
                elif board[i*3][k*3] != '.':
                    return False

                if board[i*3+1][k*3] not in st and board[i*3+1][k*3] != '.':
                    st.add(board[i*3+1][k*3])
                elif board[i*3+1][k*3] != '.':
                    return False, '333', i, k, st

                if board[i*3+2][k*3] not in st and board[i*3+2][k*3] != '.':
                    st.add(board[i*3+2][k*3])
                elif board[i*3+2][k*3] != '.':
                    return False

                if board[i*3][k*3+1] not in st and board[i*3][k*3+1] != '.':
                    st.add(board[i*3][k*3+1])
                elif board[i*3][k*3+1] != '.':
                    return False

                if board[i*3+1][k*3+1] not in st and board[i*3+1][k*3+1] != '.':
                    st.add(board[i*3+1][k*3+1])
                elif board[i*3+1][k*3+1] != '.':
                    return False

                if board[i*3+2][k*3+1] not in st and board[i*3+2][k*3+1] != '.':
                    st.add(board[i*3+2][k*3+1])
                elif board[i*3+2][k*3+1] != '.':
                    return False



                if board[i*3][k*3+2] not in st and board[i*3][k*3+2] != '.':
                    st.add(board[i*3][k*3+2])
                elif board[i*3][k*3+2] != '.':
                    return False

                if board[i*3+1][k*3+2] not in st and board[i*3+1][k*3+2] != '.':
                    st.add(board[i*3+1][k*3+2])
                elif board[i*3+1][k*3+2] != '.':
                    return False

                if board[i*3+2][k*3+2] not in st and board[i*3+2][k*3+2] != '.':
                    st.add(board[i*3+2][k*3+2])
                elif board[i*3+2][k*3+2] != '.':
                    return False

        return True

p = Solution()
print(p.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]), '  ==  True')
print(p.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]), '  ==  False')