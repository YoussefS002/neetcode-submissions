class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r=0,0
        for i in range(1, len(prices)):
            if prices[i]<prices[l]:
                l, r = i, i
            elif prices[i]>prices[r]:
                r=i
            profit=max(profit, prices[r]-prices[l])
        return profit