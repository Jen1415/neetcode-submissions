class Solution:
    @classmethod
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # selling today will beat the max_profit or not
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            # find lowest price so far
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit

