class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[None for i in range(len(s))]
        def dfs(i):
            if i==len(s):
                return 1
            if s[i]=="0":
                return 0
            if dp[i] is not None:
                return dp[i]
            decode_one=dfs(i+1)
            decode_two=dfs(i+2) if (i+1<len(s) and 10<=int(s[i:i+2])<=26) else 0
            dp[i]=decode_one+decode_two
            return dp[i]
        return dfs(0)