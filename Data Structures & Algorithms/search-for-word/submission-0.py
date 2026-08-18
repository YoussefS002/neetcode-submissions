class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nbrows=len(board)
        nbcols=len(board[0])
        def aux(i, j, currentWord, vis):
            # returns true if we can we construct word starting
            # from currentWord and adding board[i][j]
            if len(currentWord)==len(word):
                return False
            if (i, j) in vis:
                return False
            if not 0 <= i < nbrows:
                return False
            if not 0 <= j < nbcols:
                return False
            vis.add((i, j))
            currentWord+=board[i][j]
            if currentWord == word:
                return True
            res = False
            for k, l in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                res = res or aux(i+k, j+l, currentWord, vis)
            currentWord=currentWord[:-1]
            vis.remove((i, j))
            return res
                        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if aux(i, j, "", set()):
                    return True
        return False