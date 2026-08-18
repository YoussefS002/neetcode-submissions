class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo=[{} for _ in range(len(coins))]
        def aux(start_idx, amount):
            if amount==0:
                return 1
            if amount in memo[start_idx]:
                return memo[start_idx][amount]
            s=0
            for i in range(start_idx, len(coins)):
                if coins[i]>amount:
                    break
                s+=aux(i, amount-coins[i])
            memo[start_idx][amount]=s
            return s
        return aux(0, amount)