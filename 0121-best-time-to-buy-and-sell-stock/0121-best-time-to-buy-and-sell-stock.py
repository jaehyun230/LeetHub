class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        now_min = 10**5
        
        for price in prices :
            if price < now_min :
                now_min = price
            elif now_min < price :
                profit = max(profit, price-now_min)
        
        return profit