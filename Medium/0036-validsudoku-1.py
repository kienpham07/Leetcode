# Question 36 (Leetcode): Valid Soduku - Solution 1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] == ".":
                    continue
                else:
                    temp = board[x][y]

                    for i in range(0, 9):
                        if (board[i][y] == temp and i != x):
                            return False

                    for j in range(0, 9):
                        if (board[x][j] == temp and j != y):
                            return False

                    row_rigid = (x // 3) * 3 # Important
                    col_rigid = (y // 3) * 3 # Important

                    for i in range(row_rigid, row_rigid + 3):
                        for j in range(col_rigid, col_rigid + 3):
                            if (board[i][j] == temp) and (i != x or j != y):
                                return False

        return True