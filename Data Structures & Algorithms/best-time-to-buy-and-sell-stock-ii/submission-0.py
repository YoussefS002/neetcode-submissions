class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell=0,0
        profit=0
        for i in range(1, len(prices)):
            if prices[i]>prices[sell]:
                profit+=prices[i]-prices[sell]
                sell=i
            elif prices[i]<prices[sell]:
                buy = i
                sell = i
        return profit