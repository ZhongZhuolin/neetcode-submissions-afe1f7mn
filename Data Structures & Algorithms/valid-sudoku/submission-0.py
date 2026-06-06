class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
                row_set = set()
                col_set = set()
                for j in range(9):
                        if board[i][j] in row_set and board[i][j] != '.':
                                return False
                        if board[j][i] in col_set and board[j][i] != '.':
                                return False
                        if board[i][j] != '.':
                                row_set.add(board[i][j])
                        if board[j][i] != '.':
                                col_set.add(board[j][i])
        for bi in range(3):
                for bj in range(3):
                        box_set = set()
                        for i in range(3):
                                for j in range(3):
                                        val = board[bi*3 + i][bj*3 + j]
                                        if val != '.' and val in box_set:
                                                return False
                                        if val != '.':
                                                box_set.add(val)
        return True

