class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp=[[None for _ in range(len(coins))] for am in range(amount+1)]
        def res(am, i):
            if am == 0:
                return 1
            if am < 0 or i == len(coins):
                return 0
            if dp[am][i] is not None:
                return dp[am][i]
            use = res(am-coins[i], i)
            skip = res(am, i+1)
            dp[am][i] = use+skip
            return use+skip
        return res(amount, 0)