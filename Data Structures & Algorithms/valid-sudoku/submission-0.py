class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(len(board))]
        cols = [{} for i in range(len(board))]
        threes = [{} for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                three = i // 3 + j // 3 * 3
                if val in rows[i] and val != '.':
                    return False
                if val in cols[j] and val != '.':
                    return False
                if val in threes[three] and val != '.':
                    return False
                rows[i][val] = True
                cols[j][val] = True
                threes[three][val] = True
                
        return True