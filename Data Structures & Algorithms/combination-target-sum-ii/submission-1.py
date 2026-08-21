class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i, amount, comb):
            if amount==0:
                res.append(comb)
                return
            if i==len(candidates) or amount < 0:
                return
            k=1
            while i+k<len(candidates) and candidates[i+k]==candidates[i]:
                k+=1
            dfs(i+1, amount-candidates[i], comb+[candidates[i]])
            dfs(i+k, amount, comb)
        dfs(0, target, [])
        return res
            
                       