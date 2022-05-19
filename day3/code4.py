


class Solution(object):
    def exist(self, board, word):
        rows, columns, path = len(board), len(board[0]), set()
    
    def backtrack(row, col, idx):
        if idx == len(word):
            return True
        
        if (row<0 or col<0 or row>=rows or col>=columns or word[idx] != board[row][col] or (row,col) in path):
            return False
        
        path.add((row, col))
        
        res = backtrack(row+1, col, idx+1) or backtrack(row-1, col, idx+1) or backtrack(row, col-1, idx+1) or backtrack(row, col+1, idx+1)
        
        path.remove((row, col))
        
        return res
    
    
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == word[0]:
                if backtrack(i,j,0): return True
                
    return False
