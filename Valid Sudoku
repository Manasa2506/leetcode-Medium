class Solution(object):
    def isValidSudoku(self, board):
        seen = []
        
        for i, row in enumerate(board):
            for j, d in enumerate(row):
                if  d != ".":
                    seen.extend([(d,i), (j,d), (d,i//3,j//3)])    # these tuples never interfere
        
        return len(set(seen)) == len(seen)
