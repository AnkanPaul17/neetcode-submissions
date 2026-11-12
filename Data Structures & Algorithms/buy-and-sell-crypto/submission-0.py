class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=2**31
        for i in range(len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
            profit=prices[i]-minPrice
            maxProfit=max(profit, maxProfit)
        return maxProfit
            
        