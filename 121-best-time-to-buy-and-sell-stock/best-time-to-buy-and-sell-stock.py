class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        best_sell = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best_sell:
                best_sell = price - min_price

        return best_sell