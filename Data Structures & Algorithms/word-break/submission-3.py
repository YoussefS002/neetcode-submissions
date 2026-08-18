class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo=[None for _ in range(len(s))]
        def aux(i):
            if i==len(s):
                return True
            if memo[i] is not None:
                return memo[i]
            res=False
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    res=res or aux(i+len(word))
            memo[i]=res
            return memo[i]
        return aux(0)