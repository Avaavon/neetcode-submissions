"""
backtracking

time = r * c * 4^(len(word))
space = len(word)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def backtrack(r, c, i):
            # base cases
            # found
            if i == len(word):
                return True
            
            # out of bounds or not equal or already visited
            if (r<0 or r >= ROW or c<0 or c >= COL or
                board[r][c] != word[i] or
                board[r][c] == '#'):
                return False
            
            board[r][c] = '#'

            res = (
                backtrack(r-1,c, i+1) or
                backtrack(r+1,c, i+1) or 
                backtrack(r,c-1, i+1) or 
                backtrack(r,c+1, i+1)
            )
            board[r][c] = word[i]
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack (r, c, 0):
                    return True
        return False





