class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp=[[0 for i in range(len(coins))] for am in range(amount+1)]
        for i in range(len(coins)):
            dp[0][i]=1
        for am in range(1, amount+1):
            for i in range(len(coins)):
                dp[am][i]=dp[am][i-1]
                if coins[i]<=am:
                    dp[am][i]+=dp[am-coins[i]][i]
        return dp[-1][-1]