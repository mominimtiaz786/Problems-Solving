class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        block = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                elif board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                
                elif board[r][c] in block[(r//3) * 3 + c//3]:
                    return False

                else:
                    rows[r].add(board[r][c])  
                    cols[c].add(board[r][c])  
                    block[(r//3) * 3 + c//3].add(board[r][c])  
        
        return True