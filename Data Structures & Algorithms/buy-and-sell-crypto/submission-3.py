class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i, price in enumerate(prices):
            if price < lowest:
                lowest = price
            else:
                if price - lowest > max_profit:
                    max_profit = price - lowest
        return max_profit            

        
        

            