class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis=set()
        def dfs(i,j,word):
            if not word:
                return True
            if (not 0<=i<len(board)) or (not 0<=j<len(board[0])):
                return False 
            if board[i][j]!=word[0]:
                return False
            if (i,j) in vis:
                return False
            vis.add((i,j))
            directions=[
                (i, j-1),
                (i, j+1),
                (i-1, j),
                (i+1, j)
            ]
            res=False
            for k, l in directions:
                res=res or dfs(k,l,word[1:])
            vis.remove((i,j))
            return res
        res=False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res=res or dfs(i,j,word)
        return res
