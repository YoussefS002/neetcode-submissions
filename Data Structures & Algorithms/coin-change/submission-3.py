class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[[float("inf") for i in range(len(coins))] for am in range(amount+1)]
        dp[0]=[0 for coin in coins]
        for am in range(1, amount+1):
            for i in range(len(coins)):
                dp[am][i]=min(1+dp[am-coins[i]][i] if am-coins[i]>=0 else float("inf"), dp[am][i-1])
        return dp[amount][-1] if dp[amount][-1] != float("inf") else -1